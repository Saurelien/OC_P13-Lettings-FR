from django.test import TestCase
from django.urls import reverse
from lettings.models import Letting, Address


class IndexTestCase(TestCase):
    def test_index(self):
        response = self.client.get(reverse('lettings:index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/index.html')

    def setUp(self):
        """
        https://docs.python.org/3.12/library/unittest.html#unittest.TestCase.setUp
        :return:
        """
        self.address = Address.objects.create(
            number="123",
            street="Test St",
            city="Test City",
            state="TC",
            zip_code="12345",
            country_iso_code="Test Country"
        )
        self.letting = Letting.objects.create(
            title="Test Letting",
            address=self.address
        )

    def test_address_string_representation(self):
        self.assertEqual(str(self.address), "123 Test St")

    def test_address_creation(self):
        self.assertIsInstance(self.address, Address)

    def test_address_field_validations(self):
        self.assertEqual(self.address.number, "123")
        self.assertEqual(self.address.city, "Test City")
        self.assertEqual(self.address.state, "TC")
        self.assertEqual(self.address.zip_code, "12345")
        self.assertEqual(self.address.country_iso_code, "Test Country")

    def test_letting_creation(self):
        self.assertIsInstance(self.letting, Letting)

    def test_letting_string_representation(self):
        self.assertEqual(str(self.letting), "Test Letting")

    def test_letting_related_address(self):
        self.assertEqual(self.letting.address, self.address)

    def test_letting_with_valid_id(self):
        response = self.client.get(reverse('lettings:letting', args=[self.letting.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lettings/letting.html')

    def test_letting_not_found_returns_404(self):
        response = self.client.get('/lettings/nonexistent-letting/')
        self.assertEqual(response.status_code, 404)
        self.assertTemplateUsed(response, '404.html')

    # def test_letting_raises_500_error(self, letting_id):
    #     with self.settings(DEBUG=False):
    #         response = self.client.get(reverse('lettings:letting', args=[999999999]))
    #         self.assertEqual(response.status_code, 500)
    #         self.assertTemplateUsed(response, '500.html')


