# Create a security group
resource "aws_security_group" "sg_ping" {
  name   = "Allow Ping"
    egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    description = "egress enables to reach external resources"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_security_group_rule" "allow_ping"  {
     type = "ingress"
     from_port = 22
     to_port = 22
     protocol = "tcp"
     cidr_blocks = [ "0.0.0.0/0" ]
     security_group_id = aws_security_group.sg_ping.id
}

resource "aws_security_group_rule" "allow_8080" {
     type = "ingress"
     from_port = 80
     to_port = 80
     protocol = "tcp"
     cidr_blocks = [ "0.0.0.0/0" ]
     security_group_id = aws_security_group.sg_ping.id
}

locals {
  security_groups = {
    sg_ping = aws_security_group.sg_ping.id,
  }
}
