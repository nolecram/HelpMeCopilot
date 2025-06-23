# Azure LAMP Stack Deployment

This directory contains Terraform code for deploying a LAMP (Linux, Apache, MySQL, PHP) stack on Azure.

## Architecture

This deployment creates:

- A Linux VM running Ubuntu with Apache and PHP
- An Azure Database for MySQL server
- Networking components (VNet, Subnet, NSG, Public IP)
- A custom script extension to deploy a sample PHP application

## Prerequisites

- Azure account and subscription
- Terraform installed
- Azure CLI installed and configured

## Usage

1. Initialize Terraform:
```bash
terraform init
```

2. Create a `terraform.tfvars` file with your sensitive values:
```
mysql_admin_password = "YourStrongPasswordHere"
storage_account_name = "yourstorageaccount" # Optional
storage_account_key  = "yourstoragekey"     # Optional
```

3. Review the deployment plan:
```bash
terraform plan
```

4. Apply the configuration:
```bash
terraform apply
```

5. Access your LAMP application using the `app_url` output value.

## Security Notes

- The MySQL firewall rules in this example allow access from all IPs for demonstration purposes.
- For production use, restrict access to specific IP ranges.
- Always use strong passwords for database credentials.
- Consider enabling Private Link for the MySQL server in production environments.

## Customization

- Modify variables in `variables.tf` or override them in your `terraform.tfvars`
- Update the VM size in the LAMP module for different performance requirements
- Add additional security rules to the Network Security Group as needed
