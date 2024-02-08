from django.test import TestCase
from .models import Address
from apps.catalogs.models import State, City


# Create your tests here.
class AdressTestCase(TestCase):
    def setUp(self):
        self.data = {
            "state": "Colima",
        }
        self.rec_set = State.create(**self.data)

    def test_exists_address_model(self):
        print("BINGO", self.first_item)
