__newsletter_automation_Terraform__
------

This folder contains Terraform Configuration files to deploy newsletter_automation app.


__1. Pre-requisites__

A) [AWS credentials configuration] (https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html)

__2. Terraform-Installation__
------

A) [Terraform](https://phoenixnap.com/kb/how-to-install-terraform)

B) Run the commands at the terminal:
	1. `curl -fsSL https://apt.releases.hashicorp.com/gpg` | `sudo apt-key add -`
	
    2. `sudo apt-add-repository "deb [arch=amd64] https://apt.releases.hashicorp.com $(lsb_release -cs) main"`
	
    3. `sudo apt-get update && sudo apt-get install terraform`

C) Test the installation is successfull
         `terraform version`

__3. Steps to follow deploy app__
------

a) [Clone the newsletter_automation repo]https://github.com/qxf2/newsletter_automation.git.

b) change directory(cd) to `cd terraform`.

c) Change the default values in "variable.tf" 
    a). region - by default 'us-east-1'. Modify as per your default value. 
    
    b). profile - AWS profile - Modify as per your default value.

d) The provided Environment variables are used in Lambda creation - `CHATGPT_API_KEY`, `API_KEY_VALUE`, `ChannelID`, `Qxf2Bot_USER`, `ETC_CHANNEL` and values to be provided in `terraform.tfvars` file.

e) Create `terraform.tfvars` under `terraform` directory  with key names as `private_key_path`, `github_repo`, `github_repo_name`, `lambda_function_name`, `lambda_handler`, 
`lambda_runtime`, `lambda_filename`, `CHATGPT_API_KEY`, `API_KEY_VALUE`, `ETC_CHANNEL` and `Qxf2Bot_USER` - Modify as per your default values.

f) To format `terraform fmt --check` and to validate `terraform validate`(static analysis check- pops up errors if any).

g) Run `terraform init` - 
    Initializes a working directory and downloads the necessary provider plugins and modules and setting up the backend for storing your infrastructure's state.

h) Run `terraform plan` 
    Generate and show an execution plan (without applying it)

i) Run `terraform apply` 
    Apply the Infrastructure changes.

