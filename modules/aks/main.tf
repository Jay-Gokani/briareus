# @TODO: provider and required provider 

resource "azurerm_resource_group" "this" {
  name     = "briareus-resource-group"
  location = "UK South"
}

resource "azurerm_kubernetes_cluster" "this" {
  name                = "briareus-cluster"
  location            = azurerm_resource_group.this.location
  resource_group_name = azurerm_resource_group.this.name
  dns_prefix          = "briareus-dns-prefix"

  default_node_pool {
    name       = "default"
    node_count = 1
    vm_size    = "Standard_D2_v2"
    OSType = Linux
    os_sku = Ubuntu
    enable_auto_scaling = false
    # max_pods = 1
    # enable_node_public_ip = true
    # zones = 1
  }

  identity {
    type = "SystemAssigned"
  }

  tags = {
    Environment = "Dev"
  }
}

/*
Other potential fields to define:
Public IP
CIDR
outboundType = "loadBalancer"
Auto-upgrade profile = false
*/