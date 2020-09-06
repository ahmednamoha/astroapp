from django.db import models
from django import forms


from django.forms import ModelForm, TextInput, FileField, NumberInput
from .models import Extentions


class ExtentionsForm(ModelForm):
    class Meta:
        model = Extentions
        fields = ['exten', 'file']
        widgets = {'exten': NumberInput(
            attrs={'class': 'form-control', 'placeholder': 'Short code'})}
