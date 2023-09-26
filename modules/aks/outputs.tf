output "id" {
  value = azurerm_kubernetes_cluster.this.id
  description = "EKS ID."
}

output "kube_config" {
  value = azurerm_kubernetes_cluster.this.kube_config_raw
}

output "client_key" {
  value = azurerm_kubernetes_cluster.this.kube_config.0.client_key
  description = "Base64 encoded private key used to authenticate to the AKS cluster."
}

output "client_certificate" {
  value = azurerm_kubernetes_cluster.this.kube_config.0.client_certificate
  description = "Base64 encoded public certificate used to authenticate to the AKS cluster."
}

output "cluster_ca_certificate" {
  value = azurerm_kubernetes_cluster.this.kube_config.0.cluster_ca_certificate
  description = "Base64 encoded public CA certificate used as the root of trust for the AKS cluster."
}

output "host" {
  value = azurerm_kubernetes_cluster.this.kube_config.0.host
  description = "The AKS cluster server host."
}