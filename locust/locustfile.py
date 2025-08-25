from locust import HttpUser, task, between

class YoloUser(HttpUser):
    wait_time = between(1, 3)

    @task
    def predict(self):
        with open("test.jpg", "rb") as f:
            self.client.post("/detect", files={"file": f})
