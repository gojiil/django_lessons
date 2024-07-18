from django.db import models

"""
Поля модели «Клиент»:
— имя клиента
— электронная почта клиента
— номер телефона клиента
— адрес клиента
— дата регистрации клиента

Поля модели «Товар»:
— название товара
— описание товара
— цена товара
— количество товара
— дата добавления товара

Поля модели «Заказ»:
— связь с моделью «Клиент», указывает на клиента, сделавшего заказ
— связь с моделью «Товар», указывает на товары, входящие в заказ
— общая сумма заказа
— дата оформления заказа
"""

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=11)
    address = models.TextField()
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Name: {self.name}, email: {self.email}'

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Item: {self.name} ({self.description})'

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)
