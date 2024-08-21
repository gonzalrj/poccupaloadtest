import random

from utils import baseline_utils
from locust import task, HttpUser, between


sub_host_url = "/universitypress/subjects"
country_locale = ["/gb", "/us", "/ca", ""]


class AcaProductPageUsers(HttpUser):
    num_requests = 6807  # Number of requests per hour based on Google Analytics
    max_wait_time = round(3600 / (num_requests / baseline_utils.users_per_test_class), None)
    min_wait_time = round(max_wait_time / 2, None)
    wait_time = between(min_wait_time, max_wait_time)

    @task
    def visit_aca_subjects(self):
        subj_pages = ["/anthropology/biological-anthropology", "/anthropology", "/anthropology/anthropological-theory",
                      "/anthropology/anthropology-general-interest", "/anthropology/linguistic-anthropology",
                      "/anthropology/physical-anthropology", "/anthropology/social-and-cultural-anthropology",
                      "/archaeology", "/archaeology/ancient-near-east1", "/archaeology/archaeological-science"]

        self.client.get(random.choice(country_locale) + sub_host_url + random.choice(subj_pages))

    @task
    def visit_aca_series(self):
        series_pages = ["/economics/series/modern-cambridge-economics-series",
                        "/medicine/series/international-research-monographs-addictions",
                        "/literature/series/works-john-webster",
                        "/general-science/history-science/series/cometography",
                        "/earth-and-environmental-science/series/cambridge-paleobiology-series",
                        "/philosophy/history-philosophy/series/contemporary-philosophy-focus",
                        "/life-sciences/series/cambridge-monographs-experimental-biology",
                        "/politics-international-relations/middle-east-government-politics-and-policy/series"
                        "/cambridge-middle-east-library",
                        "/general-science/science-handbooks/series/cambridge-studies-history-medicine",
                        "/history/british-history-1066-1450/series/cambridge-studies-medieval-life-and-thought-third"
                        "-series"]

        self.client.get(random.choice(country_locale) + sub_host_url + random.choice(series_pages))

    @task
    def visit_aca_product(self):
        product_pages = ["/literature/literary-texts/romeo-and-juliet?format=CD&isbn=9780521625623",
                         "/languages-linguistics/semantics-and-pragmatics/sounds-spanish-3?format=PB&isbn"
                         "=9781108817882",
                         "/languages-linguistics/asian-language-and-linguistics/sounds-chinese",
                         "/economics/industrial-economics/pharmaceutical-innovation-incentives-competition-and-cost"
                         "-benefit-analysis-international-perspective",
                         "/history/east-asian-history/hong-kong-annual-administration-reports-18411941",
                         "/history/east-asian-history/taiwan-political-and-economic-reports-18611960",
                         "/music/music-performance/cori-spezzati",
                         "/earth-and-environmental-science/solid-earth-geophysics/mantle-convection-earth-and-planets"
                         "?format=WX&isbn=9780521798365",
                         "/music/twentieth-century-and-contemporary-music/conversation-blues-2nd-edition",
                         "/life-sciences/biological-anthropology-and-primatology/dental-anthropology"]

        self.client.get(random.choice(country_locale) + sub_host_url + random.choice(product_pages))

    @task
    def visit_aca_resources(self):
        resource_pages = ["/languages-linguistics/semantics-and-pragmatics/sounds-spanish-3#resources",
                          "/languages-linguistics/semantics-and-pragmatics/sounds-spanish#resources",
                          "/languages-linguistics/grammar-and-syntax/language-contact-europe-periphrastic-perfect"
                          "-through-history?format=PB#resources",
                          "/mathematics/geometry-and-topology/advances-two-dimensional-homotopy-and-combinatorial"
                          "-group-theory?format=PB#resources",
                          "/languages-linguistics/english-language-and-linguistics-general-interest/how-languages"
                          "-work-introduction-language-and-linguistics?format=PB#resources",
                          "/engineering/biomedical-engineering/problems-biomedical-fluid-mechanics-and-transport"
                          "-phenomena?format=AR#resources",
                          "/physics/biological-physics-and-soft-matter-physics/mechanics-cell-2nd-edition?format"
                          "=AR#resources",
                          "/languages-linguistics/sociolinguistics/sequence-organization-interaction-primer"
                          "-conversation-analysis-volume-1?format=PB#resources",
                          "/earth-and-environmental-science/hydrology-hydrogeology-and-water-resources/floods"
                          "-changing-climate-extreme-precipitation#resources",
                          "/languages-linguistics/european-language-and-linguistics/rus-comprehensive-course"
                          "-russian#resources"]

        self.client.get(random.choice(country_locale) + sub_host_url + random.choice(resource_pages))

    @task
    def visit_aca_search(self):
        search_subpath = "/universitypress/search?query="
        search_keywords = ["The King Army", "The Language of Indrajit of Orcha", "The Greek Anthology 2 Volume Set",
                           "Traders Without Trade", "America and Political Islam", "9780521635585", "9780521024846",
                           "9781108072595", "9780521385787", "9780521663946"]

        keyword = random.choice(search_keywords)
        formatted_keyword = keyword.replace(" ", "+")
        self.client.get(random.choice(country_locale) + search_subpath + formatted_keyword)
