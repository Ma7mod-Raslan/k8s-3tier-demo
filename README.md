# 🚀 Kubernetes 3-Tier Demo Application

This repository demonstrates a simple **3-tier architecture** deployed on Kubernetes:

- **Frontend**: Nginx (Reverse Proxy, NodePort)
- **Backend**: Flask App (ClusterIP)
- **Database**: PostgreSQL (ClusterIP, PV/PVC)

---

## 🏗️ Architecture
![Architecture Diagram](/diagrams/architecture.png)

---

## 📂 Structure
- `manifests/namespace.yml` → Namespace `demo`
- `manifests/db.yml` → ConfigMap, Secret, PV, PVC, Deployment, Service for Postgres
- `manifests/backend.yml` → ConfigMap, Deployment, Service for Flask app
- `manifests/frontend.yml` → ConfigMap (nginx.conf), Deployment, Service (NodePort)

---

## ⚡ How to Run
```bash
# Create namespace
kubectl apply -f manifests/namespace.yml

# Apply database resources
kubectl apply -f manifests/db.yml

# Apply backend resources
kubectl apply -f manifests/backend.yml

# Apply frontend resources
kubectl apply -f manifests/frontend.yml
