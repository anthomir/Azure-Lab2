from locust import HttpUser, task, between

class NumericalIntegrationUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def numerical_integration_task(self):
        lower = 0
        upper = 3.14159
        response = self.client.get('https://azureintegralfunctionpython.azurewebsites.net/api/numericalintegralservice?code=-F5PwhD4RWuP6crXj1H6pHqGDUnN3N1B8n4BnHR9CNjsAzFupx4DFw%3D%3D')
        print(response.text)
