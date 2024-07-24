from django.urls import path
from .views import hello, HelloView, Shop, hello_view

urlpatterns = [
    path('hello', hello, name='hello'),
    path('helloview', HelloView.as_view(), name='helloview'),
    path('shop/<int:client>/<int:days>', Shop.as_view(), name='shop'),
    path('', hello_view, name='index')
]