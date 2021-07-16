
from django.forms import ModelForm 
from django import forms
from .models import VaccineStatus 

# form to create
class createForm(ModelForm):
    class Meta:
        model = VaccineStatus 
        fields = '__all__'

class createForm2(ModelForm):
    class Meta:
        model = VaccineStatus 
        exclude = ('user', 'status')
        fields = '__all__'


