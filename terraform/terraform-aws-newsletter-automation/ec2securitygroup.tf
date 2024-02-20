/* Security group- Create an AWS security group named "Newsletter_Automation-sg" 
allowing SSH and HTTP traffic ingress and all egress traffic.
*/
resource "aws_security_group" "newsletter_sg" {
  name        = "Newsletter_Automation-sg"
  description = "Security group for Newsletter EC2 instance"
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    description = "ssh access"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    description = "Ingress enables external traffic to reach"
    cidr_blocks = ["0.0.0.0/0"]
  }

  # Add any additional ingress rules as needed

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    description = "egress enables to reach external resources"
    cidr_blocks = ["0.0.0.0/0"]
  }
  tags = {
    Name = "newsletter-automation-sg"
  }

}