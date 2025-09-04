from ultralytics import YOLO
from functools import lru_cache

# Function to load the YOLO model
# - @lru_cache ensures it's only loaded once per process
# - Saves memory and avoids reloading on every request
@lru_cache(maxsize=1)
def get_model():
    return YOLO("yolov8n.pt")  # Use small YOLOv8 model for speed

# Run inference on an input image
def predict_image(img):
    model = get_model()   # Load/reuse YOLO model
    results = model(img)
    detections = []

    # Iterate over predictions
    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])          # class index
            conf = float(box.conf[0])         # confidence score
            name = model.names[cls_id]        # class label

            detections.append({
                "class": name,
                "confidence": conf,
                "box": box.xyxy[0].tolist()   # [x1, y1, x2, y2]
            })
    return detections
