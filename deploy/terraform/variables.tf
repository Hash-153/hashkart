variable "aws_region" {
  description = "Primary AWS deployment region"
  type        = string
  default     = "ap-south-1" # Mumbai
}

variable "environment" {
  description = "Deployment environment (production, staging, dev)"
  type        = string
  default     = "production"
}

variable "vpc_cidr" {
  description = "CIDR block for main VPC"
  type        = string
  default     = "10.100.0.0/16"
}

variable "domain_name" {
  description = "Root domain for NovaMart Marketplace"
  type        = string
  default     = "novamart.in"
}

variable "eks_cluster_version" {
  description = "Kubernetes control plane version"
  type        = string
  default     = "1.29"
}

variable "eks_node_instance_types" {
  description = "EC2 instance types for EKS managed node groups"
  type        = list(string)
  default     = ["c6i.2xlarge", "c6a.2xlarge", "m6i.2xlarge"]
}

variable "aurora_instance_class" {
  description = "Aurora PostgreSQL database instance size"
  type        = string
  default     = "db.r6g.2xlarge"
}

variable "aurora_replica_count" {
  description = "Number of read replicas in Aurora cluster"
  type        = number
  default     = 3
}

variable "elasticache_node_type" {
  description = "ElastiCache Redis / Valkey node type"
  type        = string
  default     = "cache.r6g.xlarge"
}

variable "elasticache_num_shards" {
  description = "Number of Redis cluster shards for distributed caching"
  type        = number
  default     = 3
}
