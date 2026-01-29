from locust import HttpUser, task, between
import random

class MyEventsUser(HttpUser):
    wait_time = between(0.5, 1.5)

    @task
    def view_my_events(self):
        user_id = random.randint(1, 1000)
        page = random.randint(1, 5)

        self.client.get(
            f"/my-events?user=user_{user_id}&page={page}&limit=5",
            headers={
                "Authorization": "Bearer dummy_token",
                "Accept": "application/json"
            }
        )
