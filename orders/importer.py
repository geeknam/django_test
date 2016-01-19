import io
import csv
from orders import models

"""
Setup guide:
1. Generate test data:
    Stage 1: "manage.py generate_test_data test_data.csv --settings=django_test.settings" - generates 2k lines
    Stage 2: "manage.py generate_test_data test_data.csv 10000 --settings=django_test.settings" - generates 10k lines

2. Reset database state, do this before every import:
    manage.py reset --settings=django_test.settings

    
Deliverables:

    1. Fix the bug, make the code run. 
    2. Make the import more performant.
    3. Report meaningful errors

"""


def import_data(data):

    sio = io.StringIO(unicode(
        data.read(), errors='ignore'
    ), newline=None)

    reader = csv.DictReader(sio, dialect='excel')
    lines_imported = 0

    for row in reader:
        product, created = models.Product.objects.get_or_create(
            code=row['product_code'],
            name=row['product_name']
        )

        customer, created = models.Customer.objects.get_or_create(
            full_name=row['full_name'],
            email=row['email']
        )

        order, created = models.Order.objects.get_or_create(
            order_code=row['order_code'],
            address=row['address'],
            city=row['city'],
            postcode=row['postcode'],
            customer=customer
        )

        order_item, created = models.OrderItem.objects.get_or_create(
            order=order,
            product=product,
            quantity=row['quantity']
        )

        if created:
            lines_imported += 1

    return lines_imported