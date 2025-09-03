# Import YOLO from ultralytics package
from ultralytics import YOLO

# Load a pre-trained YOLOv8 nano model
# (small and fast, good for testing/demo purposes)
model = YOLO("yolov8n.pt")  

def predict_image(img):
    """
    Run YOLO object detection on an image.

    Args:
        img (PIL.Image or ndarray): The input image.

    Returns:
        list: A list of detections, where each detection is a dict
              containing class name, confidence, and bounding box.
    """
    # Perform inference on the input image
    results = model(img)  
    detections = []

    # Iterate through all prediction results
    for r in results:
        # Loop through each detected bounding box
        for box in r.boxes:
            # Get predicted class ID (integer)
            cls_id = int(box.cls[0])

            # Get confidence score (float)
            conf = float(box.conf[0])

            # Map class ID to class name (e.g., 'person', 'car')
            name = model.names[cls_id]

            # Append detection info as a dictionary
            detections.append({
                "class": name,                          # Detected object class
                "confidence": conf,                     # Confidence score
                "box": box.xyxy[0].tolist()             # Bounding box [x1, y1, x2, y2]
            })
    
    # Return all detections
    return detections
