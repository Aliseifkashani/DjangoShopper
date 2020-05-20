from django.db import models
from django import forms


class User(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)
    picture = models.CharField(max_length=300)
    asset = models.IntegerField()
    purchased = []

    def __str__(self):
        return self.firstName + ' ' + self.lastName
