provider "google" {
  project = var.project_id
  region  = var.region
}

resource "google_compute_instance" "lamp_vm" {
  name         = "lamp-vm"
  machine_type = "f1-micro"
  zone         = var.zone

  boot_disk {
    initialize_params {
      image = "debian-cloud/debian-9"
    }
  }

  network_interface {
    network = var.network
    access_config {
      // Ephemeral IP
    }
  }

  metadata_startup_script = <<-EOF
    #!/bin/bash
    apt-get update
    apt-get install -y apache2 mysql-server php libapache2-mod-php php-mysql
  EOF
}

resource "google_compute_firewall" "lamp_firewall" {
  name    = "lamp-firewall"
  network = var.network

  allow {
    protocol = "tcp"
    ports    = ["22", "80", "443"]
  }
}
