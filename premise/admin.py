from django.contrib import admin
from .models import MockScanEvent, Premise

admin.site.register(MockScanEvent)
admin.site.register(Premise)

# Register your models here.
