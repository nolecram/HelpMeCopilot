output "lamp_vm_public_ip" {
  description = "The public IP address of the LAMP stack VM"
  value       = azurerm_linux_virtual_machine.lamp_vm.public_ip_address
}

output "lamp_vm_private_ip" {
  description = "The private IP address of the LAMP stack VM"
  value       = azurerm_linux_virtual_machine.lamp_vm.private_ip_address
}

output "lamp_vm_username" {
  description = "The admin username for the LAMP stack VM"
  value       = azurerm_linux_virtual_machine.lamp_vm.admin_username
}

output "lamp_vm_id" {
  description = "The ID of the LAMP stack VM"
  value       = azurerm_linux_virtual_machine.lamp_vm.id
}

output "lamp_nsg_id" {
  description = "The ID of the LAMP stack Network Security Group"
  value       = azurerm_network_security_group.lamp_nsg.id
}
