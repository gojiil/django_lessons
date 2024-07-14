from django.core.management.base import BaseCommand
from lesson2.models import Item

class Command(BaseCommand):
    help = "Create item."

    def handle(self, *args, **kwargs):
        item = Item(name="Item", description="description for item", price=9.99, quantity=10)
        ...
        item.save()
        self.stdout.write(f'{item}')