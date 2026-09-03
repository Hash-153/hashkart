module "eks" {
  source  = "terraform-aws-modules/eks/aws"
  version = "~> 20.2.0"

  cluster_name    = "novamart-production"
  cluster_version = var.eks_cluster_version

  cluster_endpoint_public_access  = true
  cluster_endpoint_private_access = true

  vpc_id                   = module.vpc.vpc_id
  subnet_ids               = module.vpc.private_subnets
  control_plane_subnet_ids = module.vpc.private_subnets

  cluster_addons = {
    coredns = {
      most_recent = true
    }
    kube-proxy = {
      most_recent = true
    }
    vpc-cni = {
      most_recent = true
    }
    aws-ebs-csi-driver = {
      most_recent = true
    }
  }

  eks_managed_node_groups = {
    general_workload = {
      min_size     = 6
      max_size     = 36
      desired_size = 12

      instance_types = var.eks_node_instance_types
      capacity_type  = "ON_DEMAND"

      labels = {
        role = "application-server"
      }

      block_device_mappings = {
        xvda = {
          device_name = "/dev/xvda"
          ebs = {
            volume_size           = 100
            volume_type           = "gp3"
            iops                  = 3000
            throughput            = 125
            encrypted             = true
            delete_on_termination = true
          }
        }
      }
    }

    spot_workers = {
      min_size     = 3
      max_size     = 24
      desired_size = 6

      instance_types = ["c6a.2xlarge", "c5a.2xlarge", "m6a.2xlarge"]
      capacity_type  = "SPOT"

      labels = {
        role = "celery-async-workers"
      }
    }
  }

  enable_cluster_creator_admin_permissions = true

  tags = {
    Tier = "Compute"
  }
}
