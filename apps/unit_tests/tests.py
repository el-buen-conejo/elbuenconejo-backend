from django.test import TestCase
from apps.addresses.models import Address

# Create your tests here.


class AddressTestCase(TestCase):
    """Test the Address model."""

    def setUp(self):
        self.address = Address(
            address="Paseo de los Abedules",
        )

    def test_create_address(self):
        self.assertTrue(isinstance(self.address, Address))
        print("The Address is a valid instance of Address")

    def test_widget(self):
        self.assertTrue(True, True)
