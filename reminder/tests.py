from django.test import TestCase
from django.test import Client
from django.urls import reverse
# Create your tests here.

class UrlTests(TestCase):

    def test_home_status_code(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
    
    def test_notas_status_code(self):
        client = Client()
        response = client.get(reverse('notas'))
        self.assertEqual(response.status_code, 200)

    def test_list_notas_status_code(self):
        client = Client()
        response = client.get(reverse('list_notas'))
        self.assertEqual(response.status_code, 200)

    def test_create_notas_status_code(self):
        client = Client()
        response = client.get(reverse('create_notas'))
        self.assertEqual(response.status_code, 200)

    def test_notificaciones_status_code(self):
        client = Client()
        response = client.get(reverse('notificaciones'))
        self.assertEqual(response.status_code, 200)
