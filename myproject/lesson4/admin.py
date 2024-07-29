from django.contrib import admin
from .models import Item, Client, Order

# Register your models here.

admin.site.register(Item)
admin.site.register(Client)
admin.site.register(Order)
