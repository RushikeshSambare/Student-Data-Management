from dataclasses import fields
from tkinter import Widget
from django import forms
from .models import user
from django.core import validators

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = user
        fields = ['name','email','password']
        widgets={
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput( render_value=True , attrs={'class':'form-control'}),
        }