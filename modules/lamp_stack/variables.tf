variable "resource_group_name" {
  description = "The name of the resource group in which to create the LAMP stack resources"
  type        = string
}

variable "location" {
  description = "The Azure location where the LAMP stack resources should be created"
  type        = string
}

variable "network_interface_id" {
  description = "The ID of the network interface to attach to the LAMP stack VM"
  type        = string
}
