from django.http import HttpResponse
import ast
from rest_framework.authtoken.models import Token

from .models import Commidity
from nilva.general import request_decorator, MyEncoder


@request_decorator
def view_products(request):
    return MyEncoder().encode({'commidities': Commidity.objects.all()})  # need to check


@request_decorator
def buy(request):
    dict_str = request.body.decode("UTF-8")
    body = ast.literal_eval(dict_str)
    sum = 0
    for product_id in body['product_ids']:
        if not Commidity.objects.filter(id=product_id):
            error = {'error': 'invalid product with id=' + str(product_id)}
            return HttpResponse(MyEncoder().encode(error))
        sum += Commidity.objects.get(id=product_id)
    user = Token.objects.get(key=request.headers['Authorization'].replace('token', '', 1)).user
    if sum > user.asset:
        error = {'error': 'no enough money to buy those!'}
        return HttpResponse(MyEncoder().encode(error))
    user.asset -= sum
    return MyEncoder().encode('Successful purchase')
