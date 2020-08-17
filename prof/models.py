from django.db import models
from django.contrib.auth import models as UserModels


class User(UserModels.User):
    picture = models.ImageField(default='/home/mohammadali/PycharmProjects/DjangoShopper/Screenshot_from_2020-08-14_22-21-31.png')
    asset = models.IntegerField()
    purchased = []

    def __str__(self):
        return self.username + ', email = ' + str(self.email)
