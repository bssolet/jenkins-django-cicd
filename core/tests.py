
from django.test import SimpleTestCase
from django.urls import reverse


class HealthCheckTests(SimpleTestCase):

    def test_health_endpoint_returns_200(self):
        response = self.client.get("/health/")

        self.assertEqual(response.status_code, 200)

    def test_health_endpoint_returns_expected_json(self):
        response = self.client.get("/health/")

        self.assertJSONEqual(
            response.content,
            {
                "status": "healthy",
                "service": "jenkins-django-cicd",
            },
        )

    def test_health_endpoint_url_name(self):
        url = reverse("health-check")

        self.assertEqual(url, "/health/")
