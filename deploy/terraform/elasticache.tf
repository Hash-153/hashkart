resource "aws_elasticache_subnet_group" "redis_subnets" {
  name       = "novamart-redis-subnet-group"
  subnet_ids = module.vpc.elasticache_subnets
}

resource "aws_security_group" "redis_sg" {
  name        = "novamart-redis-sg"
  description = "Allow inbound Redis traffic from EKS worker nodes"
  vpc_id      = module.vpc.vpc_id

  ingress {
    description     = "Redis from EKS Nodes"
    from_port       = 6379
    to_port         = 6379
    protocol        = "tcp"
    security_groups = [module.eks.node_security_group_id]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_elasticache_replication_group" "redis_cluster" {
  replication_group_id       = "novamart-redis-cluster"
  description                = "NovaMart Distributed Redis Cache Cluster"
  node_type                  = var.elasticache_node_type
  port                       = 6379
  parameter_group_name       = "default.redis7.cluster.on"
  subnet_group_name          = aws_elasticache_subnet_group.redis_subnets.name
  security_group_ids         = [aws_security_group.redis_sg.id]

  num_node_groups            = var.elasticache_num_shards
  replicas_per_node_group    = 1
  automatic_failover_enabled = true
  multi_az_enabled           = true

  at_rest_encryption_enabled = true
  transit_encryption_enabled = false

  maintenance_window         = "sun:20:00-sun:21:00"
  snapshot_retention_limit   = 7
  snapshot_window            = "19:00-20:00"

  tags = {
    Tier = "Cache"
  }
}
