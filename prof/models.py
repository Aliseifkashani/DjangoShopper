from django.db import models
from django.contrib.auth import models as UserModels


class User(UserModels.User):
    picture = models.ImageField()
    asset = models.IntegerField()
    token = None
    purchased = []

    def __str__(self):
        return self.username + ', email = ' + str(self.email)
