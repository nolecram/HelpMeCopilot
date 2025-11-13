# LAMP Stack Terraform Module

This Terraform module provisions a complete LAMP (Linux, Apache, MySQL, PHP) stack infrastructure on Azure.

## Module Overview

This reusable module creates:
- **Linux Virtual Machine** running Ubuntu 18.04 LTS
- **Apache Web Server** for serving web content
- **MySQL Database Server** for data storage
- **PHP** for server-side scripting
- **Network Security Group** with security rules for web, SSH, and database access

## Module Inputs (Variables)

### Required Variables
- `resource_group_name` - Name of the Azure resource group
- `location` - Azure region for resource deployment
- `network_interface_id` - ID of the network interface to attach to the VM

### Optional Variables
Defined in `variables.tf`:
- VM size configuration
- Storage options
- Security rule customization

## Module Outputs

Defined in `outputs.tf`:
- Virtual machine ID
- Public IP address
- Network security group ID
- Connection information

## Usage

Include this module in your Terraform configuration:

```hcl
module "lamp_stack" {
  source = "./modules/lamp_stack"
  
  resource_group_name   = azurerm_resource_group.main.name
  location              = azurerm_resource_group.main.location
  network_interface_id  = azurerm_network_interface.main.id
}
```

## Components

### Virtual Machine Configuration
- **OS**: Ubuntu Server 18.04 LTS (Canonical)
- **Size**: Standard_DS1_v2 (configurable)
- **Storage**: Standard LRS (Locally Redundant Storage)
- **Admin Username**: adminuser (configurable)

### Installed Software
The module uses `custom_data` to install:
1. **Apache2** - Web server
2. **MySQL Server** - Database server
3. **PHP** - Scripting language
4. **libapache2-mod-php** - Apache PHP module
5. **php-mysql** - PHP MySQL extension

### Network Security Rules
The Network Security Group includes rules for:
- **SSH (Port 22)** - Remote administration
- **HTTP (Port 80)** - Web traffic
- **HTTPS (Port 443)** - Secure web traffic (if configured)
- **MySQL (Port 3306)** - Database access (configure with caution)

## Security Considerations

⚠️ **Important Security Notes:**

1. **SSH Access**: The default configuration allows SSH from any IP. Restrict this in production:
   ```hcl
   source_address_prefix = "YOUR_IP_ADDRESS/32"
   ```

2. **MySQL Access**: Database port should only be accessible from trusted sources
3. **Admin Credentials**: Use SSH keys instead of passwords for VM authentication
4. **Firewall Rules**: Review and customize security rules for your specific needs
5. **Updates**: Keep the VM and software up to date with security patches

## Customization

### Changing VM Size
Edit the VM size in `main.tf`:
```hcl
size = "Standard_DS2_v2"  # More powerful instance
```

### Adding Security Rules
Add additional security rules to the Network Security Group:
```hcl
security_rule {
  name                       = "Custom_App"
  priority                   = 1004
  direction                  = "Inbound"
  access                     = "Allow"
  protocol                   = "Tcp"
  source_port_range          = "*"
  destination_port_range     = "8080"
  source_address_prefix      = "*"
  destination_address_prefix = "*"
}
```

## Module Files

- **main.tf** - Main resource definitions (VM, NSG, custom installation script)
- **variables.tf** - Input variable declarations
- **outputs.tf** - Output value definitions

## Dependencies

This module requires:
- Terraform >= 1.0
- Azure provider (azurerm)
- Existing resource group
- Network interface resource

## Integration

This module is designed to work with:
- The example in `src/ICA_Azure_AWS/lamp_stack_azure/`
- Custom Terraform configurations requiring a LAMP stack
- Multi-tier application architectures

## Example: Complete Deployment

For a complete working example including networking setup, see:
- [src/ICA_Azure_AWS/lamp_stack_azure/](../../src/ICA_Azure_AWS/lamp_stack_azure/)

## Post-Deployment

After deployment:
1. SSH into the VM using the public IP
2. Configure MySQL root password: `sudo mysql_secure_installation`
3. Configure Apache virtual hosts as needed
4. Deploy your PHP application to `/var/www/html/`
5. Set appropriate file permissions

## Troubleshooting

**VM not accessible:**
- Check Network Security Group rules
- Verify public IP is assigned
- Ensure VM is running

**Software not installed:**
- Check custom_data script execution logs: `/var/log/cloud-init-output.log`
- Manually install if needed

**MySQL issues:**
- Check MySQL service status: `sudo systemctl status mysql`
- Review MySQL error logs: `/var/log/mysql/error.log`

## Contributing

When modifying this module:
- Keep variables in `variables.tf`
- Add descriptive comments
- Update this README with changes
- Test with example configurations

---

**Note**: This is a basic LAMP stack module for development and learning. For production use, implement additional security hardening, monitoring, backup strategies, and high availability configurations.
