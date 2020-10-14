from django.db import models

# Create your models here.

from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw


class Website(models.Model):
    WebSiteName = models.CharField(max_length=200)
    qr_code = models.ImageField(upload_to='qr_codes', blank=True)

    def __str__(self):
        return str(self.WebSiteName)

    def save(self, *args, **kwargs):
        qrcode_img = qrcode.make(self.WebSiteName)
        canvas = Image.new('RGB', (380, 350), 'white')
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.WebSiteName}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)