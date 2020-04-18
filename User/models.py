from django.db import models
# Imports para modelo User
from django.contrib.auth.models import AbstractUser
from django.conf import settings

class User(AbstractUser):
    #Para verificar si la persona ya verifico su correo electronico
    codigo_acceso = models.CharField(max_length=15)