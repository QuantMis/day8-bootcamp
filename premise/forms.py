from django.forms import ModelForm 
from django import forms
from .models import Premise, MockScanEvent 

# form to create
class createForm(ModelForm):
    class Meta:
        model = Premise 
        exclude = ('user', 'qr_code')
        fields = '__all__'

class createForm2(ModelForm):
     class Meta:
        model = MockScanEvent 
        exclude = ('user', 'latitude', 'longitude')
        fields = '__all__'




