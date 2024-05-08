import json
import random
from locust import HttpUser, task, between


class WebsiteUser(HttpUser):
    """
        Own locustfile, used for load testing with Locust, a dedicated load testing tool.
        The script is provided for the chart that will be created to store the Locust files in Kubernetes.
    """
    
    wait_time = between(min_wait=0.005, max_wait=0.1) # in secs
    host = "http://10.98.188.211:8501/v1/models/saved_model" # service endpoint
    
    @task
    def my_task(self):
        random_num: float = random.randint(a=0, b=1000) + random.uniform(a=0, b=1)
        headers = {'Accept': 'application/json', 'Content-Type': 'application/json'}
        response = self.client.post(':predict',
                                    data=json.dumps({'instances': [random_num]}),
                                    headers=headers )
        pass
