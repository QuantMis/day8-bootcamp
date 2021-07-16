from django.forms import ModelForm 
from django import forms
from .models import DailyUpdates

# form to create
class createForm(ModelForm):
    class Meta:
        model = DailyUpdates 
        fields = ('title', 'content')

