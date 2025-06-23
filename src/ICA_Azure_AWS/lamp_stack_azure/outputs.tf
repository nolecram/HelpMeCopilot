output "lamp_vm_public_ip" {
  description = "The public IP address of the LAMP stack VM"
  value       = module.lamp_stack.lamp_vm_public_ip
}

output "lamp_vm_private_ip" {
  description = "The private IP address of the LAMP stack VM"
  value       = module.lamp_stack.lamp_vm_private_ip
}

output "lamp_vm_username" {
  description = "The admin username for the LAMP stack VM"
  value       = module.lamp_stack.lamp_vm_username
}

output "mysql_server_fqdn" {
  description = "The fully qualified domain name of the MySQL server"
  value       = azurerm_mysql_server.lamp_mysql.fqdn
}

output "app_url" {
  description = "The URL to access the web application"
  value       = "http://${azurerm_public_ip.lamp_public_ip.fqdn}"
}
