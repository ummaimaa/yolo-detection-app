# Import required libraries
from fastapi import FastAPI, UploadFile, File
from PIL import Image
import io
from app.model import predict_image

# Initialize FastAPI app
app = FastAPI()

# Root endpoint for health check
@app.get("/")
def root():
    return {"message": "YOLO Detection API running"}

# Endpoint for object detection
@app.post("/detect")
async def detect(file: UploadFile = File(...)):
    # Read the uploaded file as bytes
    image_bytes = await file.read()

    # Convert bytes into an image object
    img = Image.open(io.BytesIO(image_bytes))

    # Run YOLO prediction on the image
    results = predict_image(img)

    # Return the detection results as JSON
    return {"detections": results}
