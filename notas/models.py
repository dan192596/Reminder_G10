from django.db import models

# Create your models here.
class Notas(models.Model):
    Fecha = models.DateTimeField(auto_now=True)
    Titulo = models.CharField(max_length=50)
    Texto = models.CharField(max_length=100, default = "")

    def __str__(self):
        return self.Titulo