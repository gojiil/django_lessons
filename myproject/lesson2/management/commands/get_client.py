from typing import Any
from django.core.management.base import BaseCommand, CommandParser
from lesson2.models import Client

class Command(BaseCommand):
    help = "Get clients by id."

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args: Any, **options: Any) -> str | None:
        pk = options['pk']
        client = Client.objects.filter(pk=pk).first()
        self.stdout.write(f'{client}')