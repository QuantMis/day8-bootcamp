from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
import datetime
import uuid

class CustomUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mobile = models.CharField(blank=True, max_length=10)
    full_name = models.CharField(blank=True, max_length=50)
    email = models.CharField(max_length=40, default='NA')

    # TODO Enhancement
    # State field 
    # NRIC field

    USER_TYPE = [
        ('U', 'user'),
        ('A', 'admin'),
    ]
    
    STATUS = [
        ('L', 'low risk'),
        ('H', 'high risk'),
    ]

    SWAB_STATUS = [
        ('NT', 'not tested'),
        ('PV', 'positive'),
        ('NV', 'negative'),
    ]


    user_type = models.CharField(max_length=1, choices=USER_TYPE, default='U')
    user_status = models.CharField(max_length=1, choices=STATUS, default='L')
    user_location_status = models.CharField(max_length=1, choices=STATUS, default='L')
    user_swab_status = models.CharField(max_length=2, choices=SWAB_STATUS, default='NT')


    def __str__(self):
        return self.email

