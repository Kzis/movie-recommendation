from locust import HttpUser, task, between
import json

class LoadTestModel(HttpUser):
    min_wait = 1000
    max_wait = 2000

    @task
    def test_recommendations(self):
        self.client.get(
            url='/recommendations/?user_id=1&returnMetadata=true'
        )
        
    @task
    def test_features(self):
        self.client.get(
            url='/features/?user_id=18'
        )