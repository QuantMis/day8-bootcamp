from django.db import models
import datetime
import uuid
from user.models import CustomUser
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

class Premise(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    premise_name = models.CharField(null=True, blank=True, max_length=50)
    premise_address = models.CharField(null=True, blank=True, max_length=50)
    qr_code = models.ImageField(upload_to='qr_code', blank=True)

    def __str__(self):
        return str(self.premise_name)

    def save(self, *args, **kwargs ):
        data = self.premise_name
        qrcode_img = qrcode.make(data)
        canvas = Image.new('RGB', (290, 290), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qrcode_img)
        fname = f'qr_code-{self.premise_name}.png'
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(fname, File(buffer), save=False)
        canvas.close()
        super().save(*args, **kwargs)

class MockScanEvent(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)
    premise = models.ForeignKey(Premise, on_delete=models.CASCADE, null=True)
    latitude = models.CharField(null=True, blank=True, max_length=50)
    longitude = models.CharField(null=True, blank=True, max_length=50)
    created_date = models.DateTimeField(null=True, blank=True, auto_now_add=True)
    def __str__(self):
        return str(self.user)





    






