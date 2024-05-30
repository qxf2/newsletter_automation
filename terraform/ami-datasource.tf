# Retrieves the most recent Ubuntu 22.04 AMI 
# from Canonical's repository
data "aws_ami" "ubuntu" {
  most_recent = true

  filter {
    name   = "name"
    values = ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"]
  }

  filter {
    name   = "virtualization-type"
    values = ["hvm"]
  }
  # 099720109477 is the Owner account number for Canonical
  owners = ["099720109477"] # Canonical
}
