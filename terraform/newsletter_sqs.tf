/*
# SQS queue creation - 
Purpose to send a message to Lambda to trigger Test Event.
Queue -> Lambda
*/
resource "aws_sqs_queue" "lambda_trigger_sqs" {
    name                        = "urlfilterlambda-trigger-queue"
    max_message_size            = 262144
    visibility_timeout_seconds  = 60
    message_retention_seconds   = 1800
}

/* 
SQS Queue creation - Purpose to receive a message 
When a Lambda Test Event triggered Lambda -> Queue
*/
resource "aws_sqs_queue" "newsletter_sqs" {
  name                       = "newsletter_sqs"
  delay_seconds              = 90
  max_message_size           = 2048
  message_retention_seconds  = 86400
  receive_wait_time_seconds  = 10
  visibility_timeout_seconds = 60
}
# This block creates a policy for the SQS queue 'newsletter_sqs'. 
# It allows Lambda functions to send, receive, delete messages, 
# and get attributes from the SQS queue. The policy ensures the Lambda 
# function has the necessary permissions to interact with the queue.
resource "aws_sqs_queue_policy" "default_policy" {
  queue_url = aws_sqs_queue.newsletter_sqs.id

  policy = jsonencode({
    Version = "2012-10-17",
    Id      = "DefaultPolicy",
    Statement = [
      {
        Sid    = "AllowLambdaToSendMessages"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
        Action   = "sqs:SendMessage"
        Resource = [
                    aws_sqs_queue.newsletter_sqs.arn
        ]
      },
      {
        Sid    = "AllowLambdaToReceiveMessages"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
        Action   = "sqs:ReceiveMessage"
        Resource = [
                    aws_sqs_queue.newsletter_sqs.arn
        ]
      },
      {
        Sid    = "AllowLambdaToDeleteMessages"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
        Action   = "sqs:DeleteMessage"
        Resource = [
                    aws_sqs_queue.newsletter_sqs.arn
        ]
      },
      {
        Sid    = "AllowLambdaToGetQueueAttributes"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
        Action   = "sqs:GetQueueAttributes"
        Effect = "Allow",
        Resource = [
          "${aws_sqs_queue.newsletter_sqs.arn}"
        ]
      }
    ]
  })
}

/* 
  Event source mapping between the Lambda function and the new SQS 
  queue-"lambda_trigger_sqs"
*/
resource "aws_lambda_event_source_mapping" "urlfilterlambda_sqs_trigger" {
  event_source_arn = aws_sqs_queue.lambda_trigger_sqs.arn
  function_name = aws_lambda_function.newsletter_lambda.function_name
  enabled = true
  batch_size = 10
}
# This block creates a policy for the SQS queue 'lambda_trigger_sqs'. 
# It allows Lambda functions to send, receive, delete messages, 
# and get attributes from this SQS queue. The policy ensures the Lambda 
# function has the necessary permissions to interact with the queue.
resource "aws_sqs_queue_policy" "queue_to_lambda_policy" {
  queue_url = aws_sqs_queue.lambda_trigger_sqs.id

  policy = jsonencode({
    Version = "2012-10-17",
    Id      = "DefaultPolicy",
    Statement = [
      {
        Sid    = "AllowLambdaToReceiveMessages"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
        Action   = ["sqs:SendMessage",
                    "sqs:ReceiveMessage",
                    "sqs:DeleteMessage",
                    "sqs:GetQueueAttributes"
                   ]
        Resource = [aws_sqs_queue.lambda_trigger_sqs.arn]
      }
    ]
  })
}
# This block creates a permission for the Lambda function.
# It allows the specified SQS queue 'lambda_trigger_sqs' to invoke the Lambda function.
# The permission ensures that the Lambda function can be triggered by events from this SQS queue.
resource "aws_lambda_permission" "allow_queue" {
  statement_id = "AllowExecutionFromSQS"
  action = "lambda:InvokeFunction"
  function_name = aws_lambda_function.newsletter_lambda.function_name
  principal = "events.amazonaws.com"
  source_arn = aws_sqs_queue.lambda_trigger_sqs.arn
}