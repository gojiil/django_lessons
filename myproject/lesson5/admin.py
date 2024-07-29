from django.contrib import admin
from .models import Item, Client, Order

@admin.action(description="Сбросить количество до нуля")
def reset_quantity(modeladmin, request, queryset):
    queryset.update(quantity=0)

class ItemAdmin(admin.ModelAdmin):
    """Товары"""
    list_display = ['name', 'quantity', 'price']
    search_fields = ['description']
    search_help_text = 'Поиск по полю "Описание товара"'
    actions = [reset_quantity]

    fields = ['name', 'quantity', 'price', 'added_date']
    readonly_fields = ['added_date']

class ClientAdmin(admin.ModelAdmin):
    """Клиенты"""
    list_display = ['name', 'email', 'address']
    ordering = ['registration_date']

class OrderAdmin(admin.ModelAdmin):
    """Заказы"""
    list_display = ['client', 'amount', 'order_date']
    ordering = ['order_date']
    list_filter = ['order_date']

# Register your models here.

admin.site.register(Item, ItemAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Order, OrderAdmin)
