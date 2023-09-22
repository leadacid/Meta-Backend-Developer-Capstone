from django.test import TestCase
from restaurant.models import MenuItem
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.serializers import MenuItemSerializer

class MenuItemTest(TestCase):
     def test_get_item(self):
        item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item, "IceCream : 80")


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.menu_item1 = MenuItem.objects.create(name="Item 1", price=10.99)
        self.menu_item2 = MenuItem.objects.create(name="Item 2", price=8.99)

    def test_get_all_menu_items(self):
        url = reverse("menu-list")
        response = self.client.get(url)
        menu_items = MenuItem.objects.all()
        serializer = MenuItemSerializer(menu_items, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)