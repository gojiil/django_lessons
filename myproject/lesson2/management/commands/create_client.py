from django.core.management.base import BaseCommand
from lesson2.models import Client

class Command(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):
        client = Client(name="John", email="johndoe@mail.ru", phone="+1234000000", address="U.K, London, Backer st., 21")
        ...
        client.save()
        self.stdout.write(f'{client}')