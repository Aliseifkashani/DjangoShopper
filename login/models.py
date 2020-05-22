from django.db import models
from django import forms


class direct(models.Model):
    email = models.CharField(max_length=30)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)


class third_party(models.Model):
    pass
