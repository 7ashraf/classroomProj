from django.core.management.base import BaseCommand, CommandError
class Command(BaseCommand):
    def helloworld(sef, *args, **kwargs):
        print('Hellow, World!')