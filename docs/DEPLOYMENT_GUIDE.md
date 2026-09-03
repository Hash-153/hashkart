# NovaMart Zero-Downtime Deployment & Infrastructure Guide

This guide details the steps required to provision multi-region cloud infrastructure using Terraform, build production container images, and execute zero-downtime blue/green Kubernetes releases via Helm.

---

## 1. Prerequisites

- **Terraform** >= 1.7.0
- **AWS CLI** v2 configured with Administrator or DevOps role
- **kubectl** & **Helm** v3
- **Docker** & **Docker Buildx**

---

## 2. Infrastructure Provisioning via Terraform

1. **Initialize Terraform Backend**:
   ```bash
   cd deploy/terraform
   terraform init -backend-config="bucket=novamart-terraform-state-ap-south-1"
   ```
2. **Review Execution Plan**:
   ```bash
   terraform plan -out=tfplan.binary
   ```
3. **Apply Plan**:
   ```bash
   terraform apply tfplan.binary
   ```

---

## 3. Kubernetes Helm Deployment

1. **Connect to EKS Cluster**:
   ```bash
   aws eks update-kubeconfig --name novamart-production --region ap-south-1
   ```
2. **Deploy Secrets & ConfigMaps**:
   ```bash
   helm upgrade --install novamart ./deploy/k8s \
     --namespace production \
     --create-namespace \
     --values ./deploy/k8s/values.yaml \
     --set backend.image.tag="2.5.0" \
     --set frontend.image.tag="2.5.0"
   ```
3. **Monitor Rollout Status**:
   ```bash
   kubectl rollout status deployment/novamart-backend -n production
   kubectl rollout status deployment/novamart-frontend -n production
   ```

---

## 4. Local Development Docker Compose

To run the entire platform locally with hot-reloading:
```bash
docker compose -f docker-compose.yml up --build
```
- **Frontend App**: `http://localhost:5173`
- **Backend API Docs (Swagger)**: `http://localhost:8000/docs`
- **Prometheus Metrics**: `http://localhost:8000/metrics`
