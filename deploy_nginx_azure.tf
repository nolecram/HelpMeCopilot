# Terraform configuration for deploying NGINX on Azure

# Define the provider
provider "azurerm" {
  features {}
}

# Create a resource group
resource "azurerm_resource_group" "nginx" {
  name     = "nginx-resources"
  location = "East US"
}

# Create a virtual network
resource "azurerm_virtual_network" "nginx_vnet" {
  name                = "nginx-vnet"
  address_space       = ["10.0.0.0/16"]
  location            = azurerm_resource_group.nginx.location
  resource_group_name = azurerm_resource_group.nginx.name
}

# Create a subnet
resource "azurerm_subnet" "nginx_subnet" {
  name                 = "nginx-subnet"
  resource_group_name  = azurerm_resource_group.nginx.name
  virtual_network_name = azurerm_virtual_network.nginx_vnet.name
  address_prefixes     = ["10.0.1.0/24"]
}

# Create a public IP
resource "azurerm_public_ip" "nginx_public_ip" {
  name                = "nginx-public-ip"
  location            = azurerm_resource_group.nginx.location
  resource_group_name = azurerm_resource_group.nginx.name
  allocation_method   = "Static"
}

# Create a network interface
resource "azurerm_network_interface" "nginx_nic" {
  name                = "nginx-nic"
  location            = azurerm_resource_group.nginx.location
  resource_group_name = azurerm_resource_group.nginx.name

  ip_configuration {
    name                          = "nginx-ip-configuration"
    subnet_id                     = azurerm_subnet.nginx_subnet.id
    private_ip_address_allocation = "Dynamic"
    public_ip_address_id          = azurerm_public_ip.nginx_public_ip.id
  }
}

# Create a virtual machine
resource "azurerm_linux_virtual_machine" "nginx_vm" {
  name                = "nginx-vm"
  resource_group_name = azurerm_resource_group.nginx.name
  location            = azurerm_resource_group.nginx.location
  size                = "Standard_DS1_v2"
  admin_username      = "adminuser"
  network_interface_ids = [
    azurerm_network_interface.nginx_nic.id,
  ]

  os_disk {
    caching              = "ReadWrite"
    storage_account_type = "Standard_LRS"
  }

  source_image_reference {
    publisher = "Canonical"
    offer     = "UbuntuServer"
    sku       = "18.04-LTS"
    version   = "latest"
  }

  # Install NGINX
  custom_data = base64encode(<<EOF
#!/bin/bash
sudo apt update
sudo apt install -y nginx
EOF
  )
}
