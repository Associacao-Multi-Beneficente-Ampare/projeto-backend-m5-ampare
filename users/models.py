from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=14, unique=True)
    birth = models.DateField(null=True)
    telephone = models.CharField(max_length=11)
    email = models.EmailField(unique=True)
