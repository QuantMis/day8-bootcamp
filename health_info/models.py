from django.db import models
import datetime
import uuid

# import CustomUser for FK
from user.models import CustomUser

class HealthInformation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    # symptom info
    batuk = models.BooleanField(default=False, verbose_name="Batuk-batuk")
    demam = models.BooleanField(default=False, verbose_name="Demam")
    sakit_kepala = models.BooleanField(default=False, verbose_name="Sakit Kepala")
    hilang_bau = models.BooleanField(default=False, verbose_name="Hilang Bau dan Rasa")
    sukar_bernafas = models.BooleanField(default=False, verbose_name="Kesukaran Bernafas")
    lain_lain = models.TextField(null=True, blank=True, verbose_name="Lain-lain")


    # travel info
    status_pelancongan = models.BooleanField(default=False)
    lokasi_pelancongan = models.CharField(null=True, blank=True, max_length=50)

    # close contact info
    status_kontak_rapat = models.BooleanField(default=False)

    KONTAK_GROUP = [
        ('A', 'group a'),
        ('B', 'group b'),
        ('C', 'group c'),
    ]

    group_kontak_rapat = models.CharField(null=True, blank=True, max_length=1, choices=KONTAK_GROUP, default='C')

    # Date
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user
