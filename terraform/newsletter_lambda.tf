
# Clones the GitHub repository and installs dependencies using pip
# in the specified directory, choosing pip3 if available. 
resource "null_resource" "aws_lambda_repo_clone" {
  provisioner "local-exec" {
    command     = <<-EOT
    git clone ${var.github_repo}
    
    # Determine the correct pip executable (pip3 or pip) and install dependencies
    $(command -v pip3 >/dev/null && echo "pip3" || echo "pip") install -r ${var.temp_path}/${var.foldername}/${var.github_repo_name}/requirements.txt -t ${var.temp_path}/${var.foldername}/${var.github_repo_name}/
  EOT
    interpreter = ["/bin/bash", "-c"]
    working_dir = var.temp_path
    environment = {
      GIT_SSH_COMMAND = "ssh -o StrictHostKeyChecking=no"
    }
  }
}

# Creates a ZIP archive of the cloned repository to be used for the Lambda layer
data "archive_file" "zip" {
  depends_on  = [null_resource.aws_lambda_repo_clone]
  type        = "zip"
  source_dir  = "${var.temp_path}/${var.foldername}/${var.github_repo_name}"
  output_path = "${var.temp_path}/${var.zipfilename}"
}
# Creates a new Lambda layer version from the ZIP file
resource "aws_lambda_layer_version" "lambda_layer" {
  filename   = data.archive_file.zip.output_path
  layer_name = var.lambda_layer_name
}

# Lambda creation with environment variables
resource "aws_lambda_function" "newsletter_lambda" {
  depends_on    = [data.archive_file.zip]
  function_name = var.lambda_function_name
  handler       = var.lambda_handler
  runtime       = var.lambda_runtime
  timeout       = 60
  memory_size   = 128
  dead_letter_config { # DLQ offers the possibility to investigate errors or failed requests to the connected Lambda function
    target_arn = aws_sqs_queue.newsletter_sqs.arn
  }
  reserved_concurrent_executions = 100 # Adding concurrency limits can prevent a rapid spike in usage and costs
  filename                       = "${var.temp_path}/${var.zipfilename}"
  role                           = aws_iam_role.lambda_role.arn
  layers                         = [aws_lambda_layer_version.lambda_layer.arn]
  environment {
    variables = {
      CHATGPT_API_KEY        = "${var.CHATGPT_API_KEY}"
      CHATGPT_VERSION        = "${var.CHATGPT_VERSION}"
      API_KEY_VALUE          = "${var.API_KEY_VALUE}"
      employee_list          = join(",", "${var.employee_list}")
      channel_ID             = "${var.ChannelID}"
      ETC_CHANNEL            = "${var.ETC_CHANNEL}"
      Qxf2Bot_USER           = "${var.Qxf2Bot_USER}"
      SKYPE_SENDER_QUEUE_URL = aws_sqs_queue.newsletter_sqs.url
      URL                    = format("%s%s%s", var.URLprefix, aws_instance.newsletter_instance.public_ip,var.URLendpoint)
      DEFAULT_CATEGORY       = 5
    }
  }
}
# lambda role creation
resource "aws_iam_role" "lambda_role" {
  name = "lambda-role"

  assume_role_policy = <<EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Action": "sts:AssumeRole",
      "Principal": {
        "Service": "lambda.amazonaws.com"
      },
      "Effect": "Allow",
      "Sid": ""
    }
  ]
}
EOF
}
# Attaches the AWSLambdaBasicExecutionRole policy to the 
# Lambda IAM role for basic execution permissions
resource "aws_iam_role_policy_attachment" "basic_execution_role_attachment" {
  role       = aws_iam_role.lambda_role.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

# attaching sqs policy to lambda
resource "aws_iam_policy" "lambda_permissions_policy" {
  name        = "lambda-permissions-policy"
  description = "Permissions policy for Lambda to access SQS queue"

  policy = jsonencode({
    Version = "2012-10-17",
    "Statement" : [
      {
        "Action" : [
          "sqs:DeleteMessage",
          "sqs:GetQueueUrl",
          "sqs:ListQueues",
          "sqs:ChangeMessageVisibility",
          "sqs:SendMessageBatch",
          "sqs:ReceiveMessage",
          "sqs:SendMessage",
          "sqs:GetQueueAttributes",
          "sqs:ListQueueTags",
          "sqs:ListDeadLetterSourceQueues",
          "logs:CreateLogGroup",
          "logs:CreateLogStream",
          "logs:PutLogEvents",
          "lambda:CreateEventSourceMapping",
          "lambda:ListEventSourceMappings",
          "lambda:ListFunctions"
        ],
        Effect : "Allow",
        Resource : [
          "${aws_sqs_queue.newsletter_sqs.arn}",
          "${aws_sqs_queue.lambda_trigger_sqs.arn}"
        ]
      }
    ]
  })
}
# Attaches the custom permissions policy to the Lambda IAM role, 
# allowing it to interact with SQS queues
resource "aws_iam_role_policy_attachment" "lambda_policy_attachment" {
  policy_arn = aws_iam_policy.lambda_permissions_policy.arn
  role       = aws_iam_role.lambda_role.name
}
