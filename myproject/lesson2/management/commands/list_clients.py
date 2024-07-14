from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from lesson2.models import Client

class Command(BaseCommand):
    help = "Get all clients."

    def handle(self, *args: Any, **options: Any) -> str | None:
        clients = Client.objects.all()
        self.stdout.write(f'{clients}')