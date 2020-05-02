from django.test import TestCase
from .models import Notas
from .forms import NotasForm
from django.test import Client
from django.urls import reverse
# Create your tests here.

class NotasModelTests(TestCase):

    def test_get_lista_notas(self):
        client = Client()
        response = client.get(reverse('list_notas'))
        self.assertEqual(response.status_code, 200)
