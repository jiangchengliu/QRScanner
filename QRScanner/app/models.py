from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    qr_code = models.ImageField(upload_to='qr_codes/', null=True, blank=True)