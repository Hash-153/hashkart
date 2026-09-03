resource "aws_s3_bucket" "catalog_media" {
  bucket = "novamart-catalog-media-prod-ap-south-1"

  tags = {
    Name = "NovaMart Catalog Images and Media"
  }
}

resource "aws_s3_bucket_versioning" "catalog_versioning" {
  bucket = aws_s3_bucket.catalog_media.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "catalog_encryption" {
  bucket = aws_s3_bucket.catalog_media.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_cloudfront_origin_access_control" "oac" {
  name                              = "novamart-s3-oac"
  description                       = "OAC for NovaMart Catalog Media S3 Bucket"
  origin_access_control_origin_type = "s3"
  signing_behavior                  = "always"
  signing_protocol                  = "sigv4"
}

resource "aws_cloudfront_distribution" "marketplace_cdn" {
  enabled             = true
  is_ipv6_enabled     = true
  comment             = "NovaMart Global Fast CDN Distribution"
  default_root_object = "index.html"
  price_class         = "PriceClass_All"

  origin {
    domain_name              = aws_s3_bucket.catalog_media.bucket_regional_domain_name
    origin_id                = "S3-NovaMart-Media"
    origin_access_control_id = aws_cloudfront_origin_access_control.oac.id
  }

  default_cache_behavior {
    allowed_methods  = ["GET", "HEAD", "OPTIONS"]
    cached_methods   = ["GET", "HEAD"]
    target_origin_id = "S3-NovaMart-Media"

    forwarded_values {
      query_string = false
      cookies {
        forward = "none"
      }
    }

    viewer_protocol_policy = "redirect-to-https"
    min_ttl                = 0
    default_ttl            = 86400
    max_ttl                = 2592000
    compress               = true
  }

  restrictions {
    geo_restriction {
      restriction_type = "none"
    }
  }

  viewer_certificate {
    cloudfront_default_certificate = true
  }

  tags = {
    Tier = "CDN"
  }
}
