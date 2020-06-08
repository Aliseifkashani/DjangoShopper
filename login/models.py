from django.db import models
from django import forms


class Direct(models.Model):
    email = models.CharField(max_length=30)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)


class Third_party(models.Model):
    pass
