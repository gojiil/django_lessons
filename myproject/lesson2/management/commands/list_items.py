from typing import Any
from django.core.management.base import BaseCommand
from lesson2.models import Item

class Command(BaseCommand):
    help = "Get all items."

    def handle(self, *args: Any, **options: Any) -> str | None:
        items = Item.objects.all()
        self.stdout.write(f'{items}')