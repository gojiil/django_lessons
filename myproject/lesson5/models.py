from django.db import models

# Create your models here.

class Client(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    phone = models.CharField(max_length=11)
    address = models.TextField(null=True, blank=True)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Name: {self.name}, email: {self.email}'

class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveSmallIntegerField(default=1)
    image = models.CharField(max_length=1000, null=True, blank=True)
    added_date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'Item: {self.name} ({self.description})'
    
    @property
    def total_quantity(self):
        return sum(item.quantity for item in Item.objects.all())

class Order(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    items = models.ManyToManyField(Item)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    order_date = models.DateTimeField(auto_now_add=True)