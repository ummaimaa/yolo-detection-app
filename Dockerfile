FROM python:3.10-slim

WORKDIR /app

# Install system dependencies for YOLO + PIL
RUN apt-get update && apt-get install -y libgl1 libglib2.0-0 && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Uvicorn runs on port 8000 inside container
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
