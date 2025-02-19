output "lamp_vm_public_ip" {
  description = "The public IP address of the LAMP stack VM"
  value       = google_compute_instance.lamp_vm.network_interface[0].access_config[0].nat_ip
}

output "lamp_vm_private_ip" {
  description = "The private IP address of the LAMP stack VM"
  value       = google_compute_instance.lamp_vm.network_interface[0].network_ip
}

output "lamp_vm_username" {
  description = "The admin username for the LAMP stack VM"
  value       = "adminuser"
}
