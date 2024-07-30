from django.shortcuts import render
from django.db.models import Sum

from lesson5.models import Item

# Create your views here.

def total_in_db(request):
    total = Item.objects.aggregate(Sum('quantity'))
    context = {
        'title': 'Sum quantity of items in bd',
        'total': total,
    }
    return render(request, 'total_count.html', context)

def total_in_view(request):
    items = Item.objects.all()
    total = sum(item.quantity for item in items)
    context = {
        'title': 'Sum quantity of items in view',
        'total': total,
    }
    return render(request, 'total_count.html', context)

def total_in_template(request):
    context = {
        'title': 'Sum quantity of items in template',
        'total': Item,
    }
    return render(request, 'total_count.html', context)
