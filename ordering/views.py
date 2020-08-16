from django.http import JsonResponse
import ast
from rest_framework.authtoken.models import Token
from django.core import serializers

from .models import Commidity
from nilva.general import request_decorator


@request_decorator
def view_products(request):
    data = serializers.serialize('json', Commidity.objects.all())
    return JsonResponse(data, safe=False)


@request_decorator
def buy(request):
    dict_str = request.body.decode("UTF-8")
    body = ast.literal_eval(dict_str)
    sum = 0
    for product_id in body['product_ids']:
        if not Commidity.objects.filter(id=product_id):
            return JsonResponse('invalid product with id=' + str(product_id), safe=False)
        sum += Commidity.objects.get(id=product_id)
    user = Token.objects.get(key=request.headers['Authorization'].replace('token', '', 1)).user
    if sum > user.asset:
        return JsonResponse('no enough money to buy those!', safe=False)
    user.asset -= sum
    return JsonResponse('Successful purchase', safe=False)
