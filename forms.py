from django import forms
from django.apps import apps

from .models import SuModel

class SuModelForm(forms.ModelForm):
    class Meta:
        model = SuModel
        fields = '__all__'
