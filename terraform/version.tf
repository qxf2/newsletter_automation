terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

# Define the AWS provider
provider "aws" {
  region  = var.region # Replace with your desired region
  profile = var.profile
}
# To archive lambda function requirements.
provider "archive" {
}
