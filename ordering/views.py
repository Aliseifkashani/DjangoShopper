from json import JSONEncoder

from .models import Commidity


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


def index(request):
    context = {
        'commidities': Commidity.objects.all()
    }
    return MyEncoder().encode(context)


def buy(requset, product_ids):
    pass
