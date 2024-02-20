# terraform_newsletter_automation-Terraform configuration files to deploy newsletter_automation app

Pre-requisites:
==============
A) AWS credentials configuration - 
    https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html

B) Steps on how to install Terraform.: 
    https://phoenixnap.com/kb/how-to-install-terraform

C) To test the installation sussessful, run the command
    terraform --version

Steps
=====
1) Clone the newsletter_automation repo: https://github.com/qxf2/newsletter_automation.git

2) change directory to terraform-aws-newsletter-automation

3) Change the below default values in "variable.tf"
    3a. region - by default 'us-east-1'. Modify as per your default value. 
    3b. profile - AWS profile - Modify as per your default value.

4) These values are used in Lambda creation - CHATGPT_API_KEY, API_KEY_VALUE, ChannelID, Qxf2Bot_USER, ETC_CHANNEL - values declared in "terraform.tfvars" file

5) CHATGPT_API_KEY, API_KEY_VALUE, ETC_CHANNEL and Qxf2Bot_USER - Modify as per your default values in "terraform.tfvars".

6) private_key_path - provided in "terraform.tfvars"

7) run the command 
    "terraform fmt --check" to format and 
    "terraform validate"(static analysis tool- errors pops up if any encoutered)

8) run the command: 
    "terraform init" # Initialize Terraform in the current directory

9) run the command" 
    "terraform plan" # Generate and show an execution plan (without applying it) 

10) run the command 
    "terraform apply" # apply the changes.