from locust import HttpUser, task, between

class NumericalIntegrationUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def numerical_integration_task(self):
        lower = 0
        upper = 3.14159
        response = self.client.get(f'/numericalintegralservice/{lower}/{upper}')
        print(response.text)
