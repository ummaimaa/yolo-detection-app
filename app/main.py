from fastapi import FastAPI, UploadFile, File
from PIL import Image
import io
from app.model import predict_image

app = FastAPI()

@app.get("/")
def root():
    return {"message": "YOLO Detection API running"}

@app.post("/detect")
async def detect(file: UploadFile = File(...)):
    image_bytes = await file.read()
    img = Image.open(io.BytesIO(image_bytes))

    results = predict_image(img)
    return {"detections": results}
