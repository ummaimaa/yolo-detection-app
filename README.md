# YOLO Object Detection API with FastAPI, Nginx & Locust

This project provides a simple **object detection API** using [YOLOv8](https://github.com/ultralytics/ultralytics) served with **FastAPI**.  
The app is containerized with **Docker** and uses **Nginx** as a reverse proxy.  
We also include **Locust** for load testing the deployed API.

---

## 🚀 Getting Started

### 1️⃣ Build and run with Docker Compose
```bash
docker compose up --build
```

### 2️⃣ Access the services

- **FastAPI Swagger UI:** [http://localhost:8080/docs](http://localhost:8080/docs)  
- **Locust UI:** [http://localhost:8089](http://localhost:8089)

---

## 🔎 API Endpoints

- **POST /detect** → Upload an image file and get detection results.  
  Example with `curl`:

  ```bash
  curl -X POST "http://localhost:8080/detect" -F "file=@locust/test.jpg"
  ```
  ---
  ## 📈 Load Testing with Locust

1. Open Locust UI at [http://localhost:8089](http://localhost:8089).  
2. Enter number of users & spawn rate, then start the test.  
3. Monitor request rate, failures, and response times in real-time.


