from django.db import models


class Commidity(models.Model):
    name = models.CharField(max_length=300)
    price = models.IntegerField()
    number = models.IntegerField()
    picture = models.CharField(max_length=300)

    def __str__(self):
        return self.name
