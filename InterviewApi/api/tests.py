from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from .models import Currency
from django.test import TestCase


class ModelTestCase(TestCase):
    def setUp(self):
        self.currencies = Currency(name="USD", value="1.3")

    def test_model_can_create_a_currency(self):
        old_count = Currency.objects.count()
        self.currencies.save()
        new_count = Currency.objects.count()
        self.assertNotEqual(old_count, new_count)


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_currency(name="", value=""):
        if name != "" and value != "":
            Currency.objects.create(name=name, value=value).save()

    def setUp(self):
        # add test data
        self.create_currency("USD", "1.32")
        self.create_currency("PLN", "21.32")
        self.create_currency("JPG", "41.32")
        self.create_currency("EUR", "51.32")

    def test_api_can_read_a_currencies(self):
        response = self.client.get(
            reverse("currency-all")
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_can_get_a_currency(self):
        currency = Currency.objects.first()
        response = self.client.get(
            reverse('currency',
            kwargs={'pk': currency.name}), format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
