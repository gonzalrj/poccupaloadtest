from locust import task, HttpUser, constant_pacing, constant_throughput, between, constant
from locust.clients import HttpSession


class HomepageBrowser(HttpUser):
    wait_time = between(180, 1500)

    @task
    def visit_homepage(self):
        self.client.get("/", name="/homepage")


