from django.core.management.base import BaseCommand
from orders import models
import random


class Command(BaseCommand):
    def handle(self, *args, **options):
        # Removes current data
        models.Customer.objects.all().delete()
        models.Product.objects.all().delete()
        models.Order.objects.all().delete()

        # Bootstrap initial data that will produce errors
        self.bootstrap()

    def bootstrap(self):
        """
        boots-trap if you know what I mean :)
        """
        for i in range(30):
            product = models.Product.objects.create(
                code='SKU%d' % random.randint(50, 300),
                name='Apple iPhone 6'
            )

        # Create some orders
        for i in range(1, 20):

            customer = models.Customer.objects.create(
                email='johnsmith%d@kgn.io' % i,
                full_name = 'John Smith'
            )

            product = models.Product.objects.create(
                code='SKU%d' % i,
                name='Apple iPhone 6'
            )

            order = models.Order.objects.create(
                order_code='ORDER%d' % i,
                address='1 Flinder St',
                city='Melbourne',
                postcode='3250',
                customer=customer,
            )

            models.OrderItem.objects.create(
                order=order,
                product=product,
                quantity=random.randint(1,9)
            )
