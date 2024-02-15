from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Category, Media, Discount, Product, Comment
from .serializers import CategorySerializer, MediaSerializer, DiscountSerializer, ProductSerializer, CommentSerializer

class CategoryTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category_data = {'name': 'Test Category'}

    def test_create_category(self):
        response = self.client.post(reverse('category-list'), self.category_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Category.objects.count(), 1)
        self.assertEqual(Category.objects.get().name, 'Test Category')

    def test_retrieve_category(self):
        category = Category.objects.create(name='Test Category')
        response = self.client.get(reverse('category-detail', kwargs={'pk': category.pk}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Test Category')



class MediaTests(TestCase):
    def setUp(self):
        self.client = APIClient()


class DiscountTests(TestCase):
    def setUp(self):
        self.client = APIClient()


class ProductTests(TestCase):
    def setUp(self):
        self.client = APIClient()


class CommentTests(TestCase):
    def setUp(self):
        self.client = APIClient()

class SerializerTests(TestCase):
    def test_category_serializer(self):
        category_data = {'name': 'Test Category'}
        serializer = CategorySerializer(data=category_data)
        self.assertTrue(serializer.is_valid())
        category = serializer.save()
        self.assertEqual(category.name, 'Test Category')

    def test_media_serializer(self):
        media_data = {'image': 'test.jpg', 'description': 'Test Media'}
        serializer = MediaSerializer(data=media_data)
        self.assertTrue(serializer.is_valid())
        media = serializer.save()
        self.assertEqual(media.description, 'Test Media')

    def test_discount_serializer(self):
        discount_data = {'type': 'percentage', 'value': '10.00', 'start_date_time': '2024-02-15T00:00:00Z', 'end_date_time': '2024-02-20T00:00:00Z', 'code': 'TEST10'}
        serializer = DiscountSerializer(data=discount_data)
        self.assertTrue(serializer.is_valid())
        discount = serializer.save()
        self.assertEqual(discount.code, 'TEST10')

    def test_product_serializer(self):
        pass

    def test_comment_serializer(self):
        pass
