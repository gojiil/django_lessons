from django.urls import path
from .views import client_form, item_form

urlpatterns = [
    path('client/add/', client_form, name='client_form'),
    path('item/add/', item_form, name='item_form')
]