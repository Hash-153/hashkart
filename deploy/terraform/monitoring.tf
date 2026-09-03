resource "aws_cloudwatch_dashboard" "marketplace_overview" {
  dashboard_name = "NovaMart-Marketplace-Production-Overview"

  dashboard_body = jsonencode({
    widgets = [
      {
        type   = "metric"
        x      = 0
        y      = 0
        width  = 12
        height = 6
        properties = {
          metrics = [
            ["AWS/ApplicationELB", "RequestCount", "LoadBalancer", module.vpc.vpc_id],
            [".", "HTTPCode_Target_5XX_Count", ".", "."],
            [".", "TargetResponseTime", ".", "."]
          ]
          period = 60
          stat   = "Sum"
          region = var.aws_region
          title  = "Ingress Traffic & Error Rate"
        }
      },
      {
        type   = "metric"
        x      = 12
        y      = 0
        width  = 12
        height = 6
        properties = {
          metrics = [
            ["AWS/RDS", "CPUUtilization", "DBClusterIdentifier", aws_rds_cluster.postgresql_primary.id],
            [".", "DatabaseConnections", ".", "."]
          ]
          period = 60
          stat   = "Average"
          region = var.aws_region
          title  = "Aurora PostgreSQL Cluster Health"
        }
      }
    ]
  })
}
