import random

from utils import baseline_utils
from locust import task, HttpUser, between


class CorpHomepageUser(HttpUser):
    num_requests = 201  # Number of requests per hour based on Google Analytics
    max_wait_time = round(3600 / (num_requests / baseline_utils.users_per_test_class), None)
    min_wait_time = round(max_wait_time / 2, None)
    wait_time = between(min_wait_time, max_wait_time)

    @task
    def visit_homepage(self):
        self.client.get("/", name="/homepage")


class BusinessHomepageUser(HttpUser):
    num_requests = 436
    max_wait_time = round(3600 / (num_requests / baseline_utils.users_per_test_class), None)
    min_wait_time = round(max_wait_time / 2, None)
    wait_time = between(min_wait_time, max_wait_time)

    @task(6)    # This task will be executed 6 times out of 10.
    # Out of 436 visits, 259 are for ELL - This will be ran 6 times more than the other tasks.
    # /cambridgeenglish does not have a Drupal homepage yet, only /english
    # TODO: To separate /cambridgeenglish when available in the future
    def visit_ell_homepage(self):
        self.client.get("/english")

    @task(2)    # This task will be executed 2 times out of 10.
    # Out of 436 visits, 81 are for EDU and IE
    # /education does not have a Drupal homepage yet, only /internationaleducation
    # TODO: To separate /education when available in the future
    def visit_edu_homepage(self):
        self.client.get("/internationaleducation")

    @task(2)    # This task will be executed 2 times out of 10.
    # Out of 436 visits, 77 are for ACA
    def visit_aca_homepage(self):
        self.client.get("/universitypress")

    @task(1)
    # Out of 436 visits, 11 are for BIB
    def visit_bib_homepage(self):
        self.client.get("/universitypress/bibles")

    @task(1)
    # Out of 436 visits, 8 are for CPE
    def visit_cpe_homepage(self):
        self.client.get("/partnership")


class CorpPageUser(HttpUser):
    num_requests = 191
    max_wait_time = round(3600 / (num_requests / baseline_utils.users_per_test_class), None)
    min_wait_time = round(max_wait_time / 2, None)
    wait_time = between(min_wait_time, max_wait_time)

    @task
    def visit_corp_pages(self):
        corp_pages = ["/about-us/annual-report", "/accessibility", "/contact-us", "/legal",
                      "/legal/candidate-privacy-notice", "/legal/conditions-of-sale-consumer",
                      "/legal/conditions-of-sale-goods", "/legal/cookies", "/legal/freedom-of-information",
                      "/legal/mobile-apps", "/legal/privacy", "/legal/safeguarding-policy",
                      "/legal/security-and-vulnerability-disclosure-policy",
                      "/legal/security-and-vulnerability-disclosure-policy/acknowledgement",
                      "/legal/website-terms-of-use", "/our-story", "/people-and-planet",
                      "/people-and-planet/anti-slavery-and-human-trafficking",
                      "/people-and-planet/diversity-and-inclusion", "/people-and-planet/environment",
                      "/rights-and-permissions", "/what-we-do"]

        corp_page = random.choice(corp_pages)
        self.client.get(corp_page)
