from django.test import TestCase
from bankapp.models import Bank, Branch, Account, AccountHolder, Transaction

# Create your tests here.
class BankModelTest(TestCase):

    def setUp(self):
        self.bank = Bank.objects.create(
            bank_name="Test Bank",
            bank_id="B1234",
            bank_type="Private",
            address="123 Test Street",
            city="Test City",
            pincode=123456,
            state="Test State",
            country="India",
            phone=1234567890,
            email="testbank@example.com",
            about="This is a test bank."
        )

    def test_bank_creation(self):
        bank = self.bank
        self.assertTrue(isinstance(bank, Bank))
        self.assertEqual(bank.__str__(), bank.bank_name)

    def test_unique_bank_id(self):
        with self.assertRaises(Exception):
            Bank.objects.create(
                bank_name="Another Bank",
                bank_id="B1234",
                bank_type="Private",
                address="456 Another Street",
                city="Another City",
                pincode=654321,
                state="Another State",
                country="India",
                phone=9876543210,
                email="anotherbank@example.com",
                about="This is another test bank."
            )

    def test_unique_phone(self):
        with self.assertRaises(Exception):
            Bank.objects.create(
                bank_name="Another Bank",
                bank_id="B5678",
                bank_type="Private",
                address="456 Another Street",
                city="Another City",
                pincode=654321,
                state="Another State",
                country="India",
                phone=1234567890,
                email="anotherbank@example.com",
                about="This is another test bank."
            )

    def test_unique_email(self):
        with self.assertRaises(Exception):
            Bank.objects.create(
                bank_name="Another Bank",
                bank_id="B5678",
                bank_type="Private",
                address="456 Another Street",
                city="Another City",
                pincode=654321,
                state="Another State",
                country="India",
                phone=9876543210,
                email="testbank@example.com",
                about="This is another test bank."
            )

    def test_default_country(self):
        bank = Bank.objects.create(
            bank_name="Default Country Bank",
            bank_id="B6789",
            bank_type="Private",
            address="789 Default Street",
            city="Default City",
            pincode=789123,
            state="Default State",
            phone=7891234560,
            email="defaultbank@example.com"
        )
        self.assertEqual(bank.country, 'India')