from django.core.management.base import BaseCommand
from orders import models

class Command(BaseCommand):
    def handle(self, *args, **options):
        models.Customer.objects.all().delete()
        models.Product.objects.all().delete()
        models.Order.objects.all().delete()

        