from django import forms
from .models import TouristDestination

class TouristDestinationForm(forms.ModelForm):
    class Meta:
        model = TouristDestination
        fields = '__all__'