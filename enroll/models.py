from tkinter import Widget
from django.db import models
from django.forms import PasswordInput

# Create your models here.
class user(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=100)    