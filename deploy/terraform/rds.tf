resource "aws_db_subnet_group" "aurora_subnets" {
  name       = "novamart-aurora-subnet-group"
  subnet_ids = module.vpc.database_subnets

  tags = {
    Name = "NovaMart Aurora Subnet Group"
  }
}

resource "aws_security_group" "aurora_sg" {
  name        = "novamart-aurora-sg"
  description = "Allow inbound PostgreSQL traffic from EKS worker nodes"
  vpc_id      = module.vpc.vpc_id

  ingress {
    description     = "PostgreSQL from EKS Nodes"
    from_port       = 5432
    to_port         = 5432
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

resource "aws_rds_cluster" "postgresql_primary" {
  cluster_identifier      = "novamart-aurora-pg-cluster"
  engine                  = "aurora-postgresql"
  engine_version          = "16.1"
  database_name           = "novamart_db"
  master_username         = "novamart_admin"
  manage_master_user_password = true

  db_subnet_group_name   = aws_db_subnet_group.aurora_subnets.name
  vpc_security_group_ids = [aws_security_group.aurora_sg.id]

  backup_retention_period = 30
  preferred_backup_window = "18:00-19:00" # UTC
  copy_tags_to_snapshot   = true
  deletion_protection     = true
  storage_encrypted       = true

  enabled_cloudwatch_logs_exports = ["postgresql"]

  tags = {
    Tier = "Database"
  }
}

resource "aws_rds_cluster_instance" "cluster_instances" {
  count              = var.aurora_replica_count
  identifier         = "novamart-aurora-instance-${count.index + 1}"
  cluster_identifier = aws_rds_cluster.postgresql_primary.id
  instance_class     = var.aurora_instance_class
  engine             = aws_rds_cluster.postgresql_primary.engine
  engine_version     = aws_rds_cluster.postgresql_primary.engine_version

  publicly_accessible = false
  monitoring_interval = 15
  auto_minor_version_upgrade = true
}
