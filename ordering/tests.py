from django.http import HttpRequest
from django.test import TestCase

from .models import Commidity


class CommidityModelTests(TestCase):

    # at first our functions didn't change number of commidity purchased
    def commidity_quantity_not_changing(self):
        commidity = Commidity.objects.get(id=1)
        quantity = commidity.number
        request = HttpRequest()
        dict = {'purchased': [commidity]}
        # creating <quantity + 1> requests buying commidity

    def Persian_named_objects(self):
        pass
