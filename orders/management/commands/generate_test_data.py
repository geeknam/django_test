from django.core.management.base import BaseCommand
import csv
import random

class Command(BaseCommand):

    def handle(self, *args, **options):
        if len(args) > 2:
            num_line = 2000
        else:
            num_line = int(args[1])
        writer = csv.DictWriter(open(args[0], 'wb'), fieldnames=[
            'email',
            'full_name',
            'product_code',
            'product_name',
            'order_code',
            'address',
            'city',
            'postcode',
            'quantity'
        ])
        writer.writeheader()

        for i in range(num_line):
            row = {}
            
            row['email'] = 'johnsmith%d@kgn.io' % i
            row['full_name'] = 'John Smith'

            row['product_code'] = 'SKU%d' % i
            row['product_name'] = 'Apple iPhone 6'

            row['order_code'] = 'ORDER%d' % i
            row['address'] = '85 Buckhurst St'
            row['city'] = 'Melbourne'
            row['postcode'] = '3250'
            row['quantity'] = random.randint(1,9)

            writer.writerow(row)


