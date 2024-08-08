from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre']

    email = models.EmailField(unique=True)
    nombre = models.CharField(max_length=70, blank=True, null=False)
    apellidoPaterno = models.CharField(max_length=70, blank=True, null=False)
    apellidoMaterno = models.CharField(max_length=70, blank=True, null=False)


