from django.forms import ModelForm 
from django import forms
from .models import HealthInformation 

# form to create
class createForm(ModelForm):
    class Meta:
        model = HealthInformation 
        exclude = ('user',)
        fields = '__all__'

