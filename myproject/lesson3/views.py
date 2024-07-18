from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.views import View
from .models import Client, Order
from datetime import datetime, timedelta

# Create your views here.

def hello(request):
    return HttpResponse("Hello from function!")

class HelloView(View):
    def get(self, request):
        return HttpResponse("Hello from class!")
    
class Shop(View):
    def get(self, request, client, days):
        client = get_object_or_404(Client, pk=client)
        res = Order.objects.filter(client=client).filter(order_date__range=(datetime.now().date - timedelta(days=days), datetime.now())).order_by('order_date')
        orders = {
            "client": client,
            "days": days,
            "orders": res
        }
        return JsonResponse(orders, json_dumps_params={"ensure_ascii": False})
    
def hello_view(request):
    context = {"name": "John"}
    return render(request, "index.html", context)