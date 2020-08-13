from django.db import models


class Commidity(models.Model):
    name = models.CharField(max_length=300)
    price = models.IntegerField(default=0)
    number = models.IntegerField(default=0)
    picture = models.ImageField()

    def __str__(self):
        return self.name
