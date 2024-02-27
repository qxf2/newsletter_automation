/*
Create a TLS private key and an AWS key pair with local-exec provisioner 
for generating and saving the private key.
*/
resource "tls_private_key" "newsletter_key" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

resource "aws_key_pair" "newsletter_generated_key" {
  key_name    = var.keyname
  public_key  = tls_private_key.newsletter_key.public_key_openssh

  provisioner "local-exec" {
    command = <<-EOT
      echo '${tls_private_key.newsletter_key.private_key_pem}' > "${var.private_key_path}/${var.keyname}.pem"
      chmod 400 "${var.private_key_path}/${var.keyname}.pem"
    EOT
  }
}

# Create an EC2 instance with volume size 30gb.
resource "aws_instance" "newsletter_instance" {
  ami                    = data.aws_ami.ubuntu.id # AMI ID
  instance_type          = var.newsletter_ec2_inst_type
  key_name                 = aws_key_pair.newsletter_generated_key.key_name
  vpc_security_group_ids = [aws_security_group.newsletter_sg.id]
  ebs_optimized          = true # Ensuring that EC2 instances are EBS-optimized will help to deliver enhanced performance for EBS workloads
  monitoring             = true # Insights about the performance and utilization of your instance
  tags = {
    "Name" : "Newsletter_automation"
  }
  root_block_device {
    volume_size = 30
    volume_type = "gp2"
    encrypted   = true
  }
  #install/start/enable docker
  provisioner "remote-exec" {
    connection {
      host        = aws_instance.newsletter_instance.public_ip
      user        = "ubuntu"
      private_key = file("${var.private_key_path}/newsletter-key-pair.pem")
    }
    inline = [
      "sudo apt-get update -y",
      "sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common",
      "curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg",
      "echo 'deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable' | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null",
      "sudo apt-get update -y",
      "sudo apt-get install -y docker.io",
      "sudo systemctl start docker",
      "sudo systemctl enable docker",
      "sudo usermod -aG docker ubuntu"
    ]
  }
  /*
  Preparing the docker image from newsletter_automation repo. 
  clone/build and run the docker image.
  */ 
  provisioner "remote-exec" {
    connection {
      host        = aws_instance.newsletter_instance.public_ip
      user        = "ubuntu"
      private_key = file("${var.private_key_path}/newsletter-key-pair.pem")
    }
    inline = [
      "cd /tmp",
      "git clone https://github.com/qxf2/newsletter_automation.git",
      "cd newsletter_automation",
      "docker build --tag newsletter_automation .",
      "sudo docker run -it -d -p 5000:5000 newsletter_automation"
    ]
  }
  # Serve newsletter-automation app, nginx download and configuration
  provisioner "remote-exec" {
    connection {
      host        = aws_instance.newsletter_instance.public_ip
      user        = "ubuntu"
      private_key = file("${var.private_key_path}/newsletter-key-pair.pem")
    }
    inline = [
      "sudo apt install nginx -y",
      "sudo apt-get install -y git",
      "cd /home/ubuntu",
      "echo going to copy file",
      "git clone https://github.com/nelabhotlaR/nginx-config-file.git",
      "sudo mv ~/nginx-config-file/nginx_config.template /etc/nginx/sites-available/default",
      "sudo nginx -t",
      "sudo systemctl restart nginx",
    ]
  }
}

# Deleting the private key while destroying the instance.
resource "null_resource" "delete_key" {
  triggers = {
    key_path = "${var.private_key_path}/${var.keyname}.pem" 
    }
provisioner "local-exec" {
  when = destroy
  command = "rm -f ${self.triggers.key_path}"
  on_failure = continue // This allows the destroy provisioner to not fail even if the file doesn't exist.
}
depends_on = [ aws_key_pair.newsletter_generated_key ]
}