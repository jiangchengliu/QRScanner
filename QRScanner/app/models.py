from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
"""
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    qr_code = models.ImageField(upload_to='qr_codes/', null=True, blank=True)

    def __str__(self):
        return self.email
class QRCode(models.Model):
user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='qr_code_user')
qr_code = models.ImageField(upload_to='qr_codes/', null=True, blank=True)

def __str__(self):
    return self.user.email
"""

class User(AbstractUser):
    pass


    
#John's models

