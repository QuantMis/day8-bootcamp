from django.db import models
import datetime
import uuid

class DailyUpdates(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.TextField(null=True, blank=True, max_length=100)
    content = models.TextField(null=True, blank=True, max_length=100)

    # Date
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

