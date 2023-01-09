from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid


class User(AbstractUser):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=50)
    cnpj = models.CharField(max_length=14, unique=True, null=True)
    birth = models.DateField(null=True)
    telephone = models.CharField(max_length=11)
    email = models.EmailField(max_length=60, unique=True) 
    
