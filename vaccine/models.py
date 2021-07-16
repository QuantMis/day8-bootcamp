from django.db import models
import datetime
from user.models import CustomUser
import uuid

class VaccineStatus(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, null=True)

    STATUS = [
        ('P','pending'),
        ('A', 'accepted'),
        ('1', 'first_dose_done'),
        ('2', 'second_dose_done'),
    ]

    TYPE = [
        ("ASTRAZENECA","AstraZeneca"),
        ("PFIZER", "PFizer"),
        ("SINOVAC", "SINOVAC"),
    ]

    LOCATION = [
        ('UM','University Malaya'),
        ('MV', 'MidValley'),
        ('PWTC', 'PWTC'),
        ('BJL', 'Bukit Jalil'),
    ]



    status = models.CharField(null=True, blank=True, max_length=1, choices=STATUS, default='P')
    vtype = models.CharField(null=True, blank=True, max_length=100, choices=TYPE, default='PFIZER')
    vplace = models.CharField(null=True, blank=True, max_length=100, choices=LOCATION, default='UM')


    # Date
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user

