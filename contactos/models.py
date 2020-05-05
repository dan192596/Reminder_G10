from django.db import models

# Create your models here.
class Contacto(models.Model):
    Nombre = models.CharField(max_length=50)
    Apodo = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    celular = models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre