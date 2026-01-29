from locust import HttpUser, task, between
import random

class EventsUser(HttpUser):
    wait_time = between(0.5, 1.5)

    @task
    def view_events(self):
        user_id = random.randint(1, 1000)
        page = random.randint(1, 5)

        self.client.get(
            f"/events?user=user_{user_id}&page={page}&limit=10",
            headers={
                "Accept": "application/json"
            }
        )
