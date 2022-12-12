
terraform {
  required_providers {
    aws = {
      source = "hashicorp/aws"
    }
  }
}

provider "aws" {
  region                  = "us-west-2"
  shared_credentials_file = "~/.aws/credentials"
  profile                 = "Vscode"
}




resource "aws_dynamodb_table" "dynamodb-1" {
  name           = "users"
  billing_mode   = "PROVISIONED"
  read_capacity  = 20
  write_capacity = 20
  hash_key       = "username"
  range_key      = "Last_name"

  attribute {
    name = "username"
    type = "S"
  }

  attribute {
    name = "Last_name"
    type = "S"
  }

  ttl {
    attribute_name = "TimeToExist"
    enabled        = false
  }

  global_secondary_index {
    name               = "usernameIndex"
    hash_key           = "username"
    range_key          = "Last_name"
    write_capacity     = 10
    read_capacity      = 10
    projection_type    = "INCLUDE"
    non_key_attributes = ["username"]
  }

  tags = {
    Name = "dynamodb-table-1"
  }
}