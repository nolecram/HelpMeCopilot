// deploy vpc in azure
resource "azurerm_resource_group" "example" {
  name     = "example-resources"
  location = "West Europe"
}