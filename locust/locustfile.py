# Import Locust classes
from locust import HttpUser, task, between

# Define a simulated user for load testing
class YoloUser(HttpUser):
    # Wait time between tasks: each user waits between 1–3 seconds
    wait_time = between(1, 3)

    # Define a task that this simulated user will repeatedly perform
    @task
    def predict(self):
        # Open a test image in binary mode
        with open("test.jpg", "rb") as f:
            # Send a POST request to the FastAPI /detect endpoint
            # Uploads the image file as multipart/form-data
            self.client.post("/detect", files={"file": f})
