
from django.forms import ModelForm 
from django import forms
from .models import VaccineStatus 

# form to create
class createForm(ModelForm):
    class Meta:
        model = VaccineStatus 
        fields = '__all__'

