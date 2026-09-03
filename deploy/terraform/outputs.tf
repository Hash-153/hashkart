output "vpc_id" {
  description = "ID of the VPC"
  value       = module.vpc.vpc_id
}

output "eks_cluster_endpoint" {
  description = "Endpoint for EKS control plane"
  value       = module.eks.cluster_endpoint
}

output "eks_cluster_name" {
  description = "Kubernetes Cluster Name"
  value       = module.eks.cluster_name
}

output "aurora_cluster_endpoint" {
  description = "Writer endpoint for Aurora PostgreSQL cluster"
  value       = aws_rds_cluster.postgresql_primary.endpoint
}

output "aurora_cluster_reader_endpoint" {
  description = "Reader endpoint for Aurora PostgreSQL cluster"
  value       = aws_rds_cluster.postgresql_primary.reader_endpoint
}

output "elasticache_primary_endpoint" {
  description = "Configuration endpoint for ElastiCache Redis cluster"
  value       = aws_elasticache_replication_group.redis_cluster.configuration_endpoint_address
}

output "cloudfront_distribution_domain_name" {
  description = "Domain name of CloudFront CDN distribution"
  value       = aws_cloudfront_distribution.marketplace_cdn.domain_name
}

output "s3_assets_bucket_name" {
  description = "S3 bucket for catalog media assets"
  value       = aws_s3_bucket.catalog_media.bucket
}
