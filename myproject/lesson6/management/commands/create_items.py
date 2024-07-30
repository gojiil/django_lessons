from random import randint, uniform
from typing import Any

from django.core.management.base import BaseCommand, CommandParser
from lesson5.models import Item

class Command(BaseCommand):
    help = 'Generate fake items.'

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument('count', type=int, help='Quantity items for generate.')

    def handle(self, *args: Any, **options: Any) -> str | None:
        items = []
        count = options.get('count')
        for i in range(1, count + 1):
            items.append(Item(
                name = f'Fake item {i}',
                description = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Morbi sed est eu lacus sodales feugiat. Sed volutpat, neque quis luctus volutpat, lectus lectus venenatis erat, nec consequat lorem dolor.',
                price = uniform(0.01, 9.99),
                quantity = randint(1, 100),
            ))
        Item.objects.bulk_create(items)