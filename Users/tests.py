from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Person, Address
from .serializers import PersonSerializer, AddressSerializer
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from . import views

class UserViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.person_data = {
            'email': 'test@example.com',
            'first_name': 'John',
            'last_name': 'Doe',
            'phone_number': '1234567890',
            'role': 'customer'
        }
        self.person = Person.objects.create(**self.person_data)
        self.person_serializer = PersonSerializer(instance=self.person)

    def test_get_person_list(self):
        url = reverse('user')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [self.person_serializer.data])

    def test_create_person(self):
        url = reverse('user')
        new_person_data = {
            'email': 'newuser@example.com',
            'first_name': 'Jane',
            'last_name': 'Smith',
            'phone_number': '9876543210',
            'role': 'product manager'
        }
        response = self.client.post(url, new_person_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Person.objects.count(), 2)  
        self.assertTrue(Person.objects.filter(email='newuser@example.com').exists())

    def test_update_person(self):
        url = reverse('user-pk', kwargs={'pk': self.person.pk})
        updated_data = {
            'first_name': 'Updated Name'
        }
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.person.refresh_from_db()
        self.assertEqual(self.person.first_name, 'Updated Name')

    def test_delete_person(self):
        url = reverse('user-pk', kwargs={'pk': self.person.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.person.refresh_from_db()
        self.assertFalse(self.person.is_active)

class AddressViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.person = Person.objects.create(email='test@example.com', first_name='John', last_name='Doe', phone_number='1234567890')
        self.address_data = {
            'person': self.person,
            'country': 'USA',
            'city': 'New York',
            'street': '123 Main St'
        }
        self.address = Address.objects.create(**self.address_data)
        self.address_serializer = AddressSerializer(instance=self.address)

    def test_get_address_list(self):
        url = reverse('address')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, [self.address_serializer.data])

    def test_create_address(self):
        url = reverse('address')
        new_address_data = {
            'person': self.person.pk,
            'country': 'Canada',
            'city': 'Toronto',
            'street': '456 Maple Ave'
        }
        response = self.client.post(url, new_address_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Address.objects.count(), 2)  # Assuming there's already one address created
        self.assertTrue(Address.objects.filter(country='Canada').exists())

    def test_update_address(self):
        url = reverse('address-pk', kwargs={'pk': self.address.pk})
        updated_data = {
            'country': 'Updated Country'
        }
        response = self.client.put(url, updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.address.refresh_from_db()
        self.assertEqual(self.address.country, 'Updated Country')

    def test_delete_address(self):
        url = reverse('address-pk', kwargs={'pk': self.address.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.address.refresh_from_db()
        self.assertFalse(self.address.is_active)


class TestUrls(SimpleTestCase):
    def test_users_url_resolves(self):
        url = reverse('user')
        self.assertEqual(resolve(url).func.view_class, views.UserView)

    def test_address_url_resolves(self):
        url = reverse('address')
        self.assertEqual(resolve(url).func.view_class, views.AddressView)