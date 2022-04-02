from django.test import TestCase
from http import HTTPStatus


# Create your tests here.
class HomeTest(TestCase):
    def test_index(self):
        result = self.client.get("/hw/")
        self.assertEqual(result.status_code, HTTPStatus.OK)

    def test_index_post(self):
        form_data = [
            {"weight": 200, "height": 100},
            {"weight": 500, "height": 100},
            {"weight": 100, "height": 200},
            {"weight": 800, "height": 800},
        ]

        for data in form_data:
            result = self.client.post("/hw/", data=data)
            self.assertEqual(result.status_code, HTTPStatus.OK)
