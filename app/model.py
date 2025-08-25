from ultralytics import YOLO

model = YOLO("yolov8n.pt")  

def predict_image(img):
    results = model(img)  
    detections = []

    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            name = model.names[cls_id]
            detections.append({
                "class": name,
                "confidence": conf,
                "box": box.xyxy[0].tolist() 
            })
    return detections
