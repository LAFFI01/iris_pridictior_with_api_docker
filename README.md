linnk="https://hub.docker.com/u/laffi01"
# 🌸 Iris Flower Prediction App

This project is a **full-stack machine learning app** to predict iris flower species.  
It consists of:

- **Backend:** FastAPI for serving the prediction API  
- **Frontend:** Streamlit web app for user interaction  
- **Deployment:** Dockerized for easy setup and portability  

---

## 🖥️ Features

- Input iris flower features (sepal length, petal width)  
- Get predicted iris species with confidence score  
- View class probabilities for all species  
- Run anywhere using Docker  

---

## 🔧 Prerequisites

Before running the app, you need:

1. **Docker** installed on your system.  
   - [Install Docker Desktop (Windows/Mac)](https://www.docker.com/get-started)  
   - [Install Docker Engine (Linux)](https://docs.docker.com/engine/install/)
2. Internet connection to pull images from Docker Hub  

---

## 📦 Docker Hub Images

The project images are hosted on Docker Hub:  

| Component | Docker Image | Tag |
|-----------|-------------|-----|
| Backend   | `laffi01/iris-backend` | `latest` |
| Frontend  | `laffi01/iris-frontend` | `latest` |

---

## 🚀 Step-by-Step Guide (From Scratch)

### **1️⃣ Pull the Docker images**
Open your terminal or PowerShell and run:

```bash
docker pull laffi01/iris-backend:latest
docker pull laffi01/iris-frontend:latest
```

---

### **2️⃣ Run the backend**
Start the FastAPI backend first:

```bash
docker run -d -p 8000:8000 --name iris-backend laffi01/iris-backend:latest
```

- `-d` → run container in detached mode  
- `-p 8000:8000` → map backend port 8000 to your local machine  
- `--name iris-backend` → name your container  

Check if it’s running:

```bash
docker ps
```

You should see `iris-backend` running on port 8000.

---

### **3️⃣ Run the frontend**
Start the Streamlit frontend next:

```bash
docker run -d -p 8501:8501 -e API_URL=http://host.docker.internal:8000/predict --name iris-frontend laffi01/iris-frontend:latest
```

- `-e API_URL=...` → tells frontend where the backend API is  
- On Linux, replace `host.docker.internal` with your backend container name:  
  ```bash
  -e API_URL=http://iris-backend:8000/predict
  ```

---

### **4️⃣ Access the App**
- Frontend (Streamlit): [http://localhost:8501](http://localhost:8501)  
- Backend (FastAPI): [http://localhost:8000](http://localhost:8000)  

You can now input iris features and get predictions!

---

### **5️⃣ Stop and remove containers**
When done, stop and remove containers:

```bash
docker stop iris-frontend iris-backend
docker rm iris-frontend iris-backend
```

---

## 📝 Optional: Run Both Together Using Docker Compose

Create a `docker-compose.yml` file:

```yaml
services:
  backend:
    image: laffi01/iris-backend:latest
    container_name: iris-backend
    ports:
      - "8000:8000"

  frontend:
    image: laffi01/iris-frontend:latest
    container_name: iris-frontend
    ports:
      - "8501:8501"
    environment:
      - API_URL=http://backend:8000/predict
    depends_on:
      - backend
```

Run both frontend and backend with one command:

```bash
docker-compose up -d
```

- Stop all containers:

```bash
docker-compose down
```

---

## 🛠️ Author

- GitHub: [laffi01](https://github.com/laffi01)

---

## ✅ Notes

- Always start the **backend first** if running manually.  
- On Linux, networking between containers may need the backend container name instead of `host.docker.internal`.  
- You can pull latest images anytime with:  
```bash
docker pull laffi01/iris-backend:latest
docker pull laffi01/iris-frontend:latest
```
