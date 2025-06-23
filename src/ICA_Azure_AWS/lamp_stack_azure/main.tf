### Azure LAMP Stack Deployment Example
# Provider configuration
provider "azurerm" {
  features {}
}

# Resource group for all resources
resource "azurerm_resource_group" "lamp_rg" {
  name     = var.resource_group_name
  location = var.location
}

# Virtual network
resource "azurerm_virtual_network" "lamp_vnet" {
  name                = "lamp-vnet"
  address_space       = ["10.0.0.0/16"]
  location            = azurerm_resource_group.lamp_rg.location
  resource_group_name = azurerm_resource_group.lamp_rg.name
}

# Subnet
resource "azurerm_subnet" "lamp_subnet" {
  name                 = "lamp-subnet"
  resource_group_name  = azurerm_resource_group.lamp_rg.name
  virtual_network_name = azurerm_virtual_network.lamp_vnet.name
  address_prefixes     = ["10.0.1.0/24"]
}

# Public IP
resource "azurerm_public_ip" "lamp_public_ip" {
  name                = "lamp-public-ip"
  location            = azurerm_resource_group.lamp_rg.location
  resource_group_name = azurerm_resource_group.lamp_rg.name
  allocation_method   = "Dynamic"
  domain_name_label   = var.domain_name_label
}

# Network interface
resource "azurerm_network_interface" "lamp_nic" {
  name                = "lamp-nic"
  location            = azurerm_resource_group.lamp_rg.location
  resource_group_name = azurerm_resource_group.lamp_rg.name

  ip_configuration {
    name                          = "internal"
    subnet_id                     = azurerm_subnet.lamp_subnet.id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = azurerm_public_ip.lamp_public_ip.id
  }
}

# Network Security Group association
resource "azurerm_network_interface_security_group_association" "lamp_nsg_association" {
  network_interface_id      = azurerm_network_interface.lamp_nic.id
  network_security_group_id = module.lamp_stack.lamp_nsg_id
}

# MySQL server
resource "azurerm_mysql_server" "lamp_mysql" {
  name                = "lamp-mysql-server"
  location            = azurerm_resource_group.lamp_rg.location
  resource_group_name = azurerm_resource_group.lamp_rg.name

  administrator_login          = var.mysql_admin_username
  administrator_login_password = var.mysql_admin_password

  sku_name   = "B_Gen5_1"
  storage_mb = 5120
  version    = "5.7"

  auto_grow_enabled                = true
  geo_redundant_backup_enabled     = false
  infrastructure_encryption_enabled = false
  public_network_access_enabled    = true
  ssl_enforcement_enabled          = true
}

# MySQL database
resource "azurerm_mysql_database" "lamp_db" {
  name                = "lampdb"
  resource_group_name = azurerm_resource_group.lamp_rg.name
  server_name         = azurerm_mysql_server.lamp_mysql.name
  charset             = "utf8"
  collation           = "utf8_general_ci"
}

# MySQL firewall rule - allow Azure services
resource "azurerm_mysql_firewall_rule" "lamp_mysql_firewall_azure" {
  name                = "AllowAzureServices"
  resource_group_name = azurerm_resource_group.lamp_rg.name
  server_name         = azurerm_mysql_server.lamp_mysql.name
  start_ip_address    = "0.0.0.0"
  end_ip_address      = "0.0.0.0"
}

# MySQL firewall rule - allow all (for development purposes only)
resource "azurerm_mysql_firewall_rule" "lamp_mysql_firewall_all" {
  name                = "AllowAll"
  resource_group_name = azurerm_resource_group.lamp_rg.name
  server_name         = azurerm_mysql_server.lamp_mysql.name
  start_ip_address    = "0.0.0.0"
  end_ip_address      = "255.255.255.255"
}

# Use our LAMP stack module
module "lamp_stack" {
  source              = "../../../modules/lamp_stack"
  resource_group_name = azurerm_resource_group.lamp_rg.name
  location            = azurerm_resource_group.lamp_rg.location
  network_interface_id = azurerm_network_interface.lamp_nic.id
}

# Deploy a sample PHP application using custom script extension
resource "azurerm_virtual_machine_extension" "lamp_app_deploy" {
  name                 = "lamp-app-deploy"
  virtual_machine_id   = module.lamp_stack.lamp_vm_id
  publisher            = "Microsoft.Azure.Extensions"
  type                 = "CustomScript"
  type_handler_version = "2.0"

  settings = <<SETTINGS
    {
      "fileUris": ["${var.script_url}"],
      "commandToExecute": "sh setup_lamp.sh"
    }
  SETTINGS

  protected_settings = {
    "storageAccountName": "${var.storage_account_name}",
    "storageAccountKey": "${var.storage_account_key}"
  }

  depends_on = [module.lamp_stack]
}
