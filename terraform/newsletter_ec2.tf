# To generate secure key pair for ec2 instance
resource "tls_private_key" "newsletter_key" {
  algorithm = "RSA"
  rsa_bits  = 4096
}

resource "aws_key_pair" "newsletter_generated_key" {
  key_name    = var.keyname
  public_key  = tls_private_key.newsletter_key.public_key_openssh

  provisioner "local-exec" {
    command = <<-EOT
      echo '${tls_private_key.newsletter_key.private_key_pem}' > "${var.temp_path}/${var.keyname}.pem"
      chmod 400 "${var.temp_path}/${var.keyname}.pem"
    EOT
  }
}

# Create an EC2 instance with volume size 30gb. 
resource "aws_instance" "newsletter_instance" {
  ami                    = data.aws_ami.ubuntu.id # AMI ID
  instance_type          = var.newsletter_ec2_inst_type
  key_name                 = aws_key_pair.newsletter_generated_key.key_name
  vpc_security_group_ids = [local.security_groups.sg_ping]
  ebs_optimized          = true # Ensuring that EC2 instances are EBS-optimized will help to deliver enhanced performance for EBS workloads
  monitoring             = true # Insights about the performance and utilization of your instances
  tags = {
    "Name" : "Newsletter_automation"
  }
  root_block_device {
    volume_size = 30
    volume_type = "gp2"
    encrypted   = true
  }
  # to install/start/enable docker
  provisioner "remote-exec" {
    connection {
      host        = aws_instance.newsletter_instance.public_ip
      user        = "${var.remoteuser}"
      private_key = file("${var.temp_path}/${var.keyname}.pem")
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
      "sudo usermod -aG docker ${var.remoteuser}"
    ]
  }
  # to prepare the docker image from Github repo 
  # newsletter_automation. Clone and run the docker image
  provisioner "remote-exec" {
    connection {
      host        = aws_instance.newsletter_instance.public_ip
      user        = "${var.remoteuser}"
      private_key = file("${var.temp_path}/${var.keyname}.pem")
    }
    inline = [
      # clone the repo
      "cd ${var.temp_path}",
      "git clone https://github.com/qxf2/newsletter_automation.git",
      "cd newsletter_automation",
      "docker build -t newsletter_automation .",
      # Run the container with a specific name
      "sudo docker run -it -d --name newsletter_automation -p 5000:5000 newsletter_automation",
      # Wait for a few seconds to ensure the container is fully up
      "sleep 15",
      # Docker exec commands to modify the setup script
      "docker exec newsletter_automation /bin/sh -c 'chmod +x /newsletter_setup.sh'",
      "docker exec newsletter_automation /bin/sh -c 'sed -i \"s/^export API_KEY=.*/export API_KEY=\\\"test\\\"/\" /newsletter_setup.sh'",
      "docker exec newsletter_automation /bin/sh -c 'cat /newsletter_setup.sh'",
      # Stop and start the Docker container to reflect changes
      "docker stop newsletter_automation",
      "docker start newsletter_automation"
    ]
  }
  # Copy the nginx template file from the local folder to the EC2 instance
  provisioner "file" {
    source      = "nginx_config.template"
    destination = "/tmp/nginx_config.template"
    connection {
      host        = aws_instance.newsletter_instance.public_ip
      user        = "${var.remoteuser}"
      private_key = file("${var.temp_path}/${var.keyname}.pem")
    }
  }
  # to serve newsletter app for nginx download and configuration
  provisioner "remote-exec" {
    connection {
      host        = aws_instance.newsletter_instance.public_ip
      user        = "${var.remoteuser}"
      private_key = file("${var.temp_path}/${var.keyname}.pem")
    }
    inline = [
      # nginx installation
      "sudo apt install nginx -y",
      #"sudo apt-get install -y git",
      #"cd ${var.homedir}",
      "echo going to copy file",
      #"git clone https://github.com/nelabhotlaR/nginx-config-file.git",
      #"sudo mv ~/nginx-config-file/nginx_config.template /etc/nginx/sites-available/default",
      "sudo mv /tmp/nginx_config.template /etc/nginx/sites-available/default",
      "sudo nginx -t",
      "sudo systemctl restart nginx",
    ]
  }
}

# deleting the private key when terminating the instance.
resource "null_resource" "delete_key" {
  triggers = {
    key_path = "${var.temp_path}/${var.keyname}.pem"
    }
provisioner "local-exec" {
  when = destroy
  command = "rm -f ${self.triggers.key_path}"
  on_failure = continue // This allows the destroy provisioner to not fail even if the file doesn't exist.
}
depends_on = [ aws_key_pair.newsletter_generated_key ]
}
# deleting the folder when terminating the instance.
resource "null_resource" "delete_folder" {
  triggers = {
    key_path = "${var.temp_path}/${var.foldername}"
  }
provisioner "local-exec" {
  when = destroy
  command = "rm -f -r ${self.triggers.key_path}"
  on_failure = continue
}
}
# deleting the zip file when terminating the instance.
resource "null_resource" "delete_zipfile" {
  triggers = {
    key_path = "${var.temp_path}/${var.zipfilename}"
  }
provisioner "local-exec" {
  when = destroy
  command = "rm -f ${self.triggers.key_path}"
  on_failure = continue
}
}