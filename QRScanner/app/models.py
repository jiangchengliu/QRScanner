from django.db import models
from django.contrib.auth.models import AbstractUser
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    qr_code = models.ImageField(upload_to='qr_codes/', null=True, blank=True)

    def __str__(self):
        return str(self.email)
    
    def save(self, *args, **kwargs):
        qrcodeimg = qrcode.make(self.email)
        canvas = Image.new('RGB', (qrcodeimg.pixel_size, qrcodeimg.pixel_size,), 'white')
        draw = ImageDraw.draw(canvas)
        canvas.paste(qrcodeimg)
        fname = f'qr_code-{self.email.png}'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)



    
#John's models

