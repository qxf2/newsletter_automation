# SQS creation
resource "aws_sqs_queue" "newsletter_sqs" {
  name                       = "newsletter_sqs"
  delay_seconds              = 90
  max_message_size           = 2048
  message_retention_seconds  = 86400
  receive_wait_time_seconds  = 10
  visibility_timeout_seconds = 60
}
# sqs policy
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
        Resource = aws_sqs_queue.newsletter_sqs.arn
      },
      {
        Sid    = "AllowLambdaToReceiveMessages"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
        Action   = "sqs:ReceiveMessage"
        Resource = aws_sqs_queue.newsletter_sqs.arn
      },
      {
        Sid    = "AllowLambdaToDeleteMessages"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
        Action   = "sqs:DeleteMessage"
        Resource = aws_sqs_queue.newsletter_sqs.arn
      },
      {
        Sid    = "AllowLambdaToGetQueueAttributes"
        Effect = "Allow"
        Principal = {
          Service = "lambda.amazonaws.com"
        }
        Action   = "sqs:GetQueueAttributes"
        Resource = aws_sqs_queue.newsletter_sqs.arn
      }
    ]
  })
}