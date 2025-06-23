variable "resource_group_name" {
  description = "The name of the resource group in which to create the LAMP stack resources"
  type        = string
  default     = "lamp-stack-rg"
}

variable "location" {
  description = "The Azure location where the LAMP stack resources should be created"
  type        = string
  default     = "eastus"
}

variable "domain_name_label" {
  description = "Domain name label for the public IP address"
  type        = string
  default     = "lamp-example"
}

variable "mysql_admin_username" {
  description = "The administrator username for the MySQL server"
  type        = string
  default     = "mysqladmin"
}

variable "mysql_admin_password" {
  description = "The administrator password for the MySQL server"
  type        = string
  sensitive   = true
}

variable "storage_account_name" {
  description = "The name of the storage account for custom script extension"
  type        = string
  default     = ""
}

variable "storage_account_key" {
  description = "The key for the storage account for custom script extension"
  type        = string
  sensitive   = true
  default     = ""
}

variable "script_url" {
  description = "URL to the LAMP setup script"
  type        = string
  default     = "https://raw.githubusercontent.com/yourusername/your-repo/main/scripts/setup_lamp.sh"
}
