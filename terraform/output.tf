# Terraform Output Values
output "instance_publicip" {
  description = "EC2 Instance Public IP"
  value       = aws_instance.newsletter_instance.public_ip
}

output "instance_publicdns" {
  description = "EC2 Instance Public DNS"
  value       = aws_instance.newsletter_instance.public_dns
}
output "lambda_function_arn" {
  value = aws_lambda_function.newsletter_lambda.arn
}

output "aws_sqs_queue" {
  value = aws_sqs_queue.newsletter_sqs.arn
}