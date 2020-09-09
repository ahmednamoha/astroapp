from django.db import models
from django import forms


from django.forms import ModelForm, TextInput, FileField, NumberInput
from .models import Extentions, Queue


class ExtentionsForm(ModelForm):
    class Meta:
        model = Extentions
        fields = ['exten', 'file']
        widgets = {'exten': NumberInput(
            attrs={'class': 'form-control', 'placeholder': 'Short code'})}


class QueueForm(ModelForm):
    class Meta:
        model = Queue
        fields = ['name', 'optin', 'exten']
        widgets = {'optin': NumberInput(
            attrs={'class': 'form-control', 'placeholder': '1'}), 'name': TextInput(
            attrs={'class': 'form-control', 'placeholder': 'queue name'})}
