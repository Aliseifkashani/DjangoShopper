from django.db import models


class Commidity(models.Model):
    name = models.CharField(max_length=300)
    price = models.IntegerField(default=0)
    number = models.IntegerField(default=0)
    picture = models.ImageField(default='/home/mohammadali/PycharmProjects/DjangoShopper/Screenshot_from_2020-08-14_22-21-31.png')

    def __str__(self):
        return self.name
