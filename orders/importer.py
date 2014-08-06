import io
import csv
from orders import models


"""
Deliverables:

    1. Make the code work
    2. Make it more performant
    3. Report meaningful errors

"""


def import_data(data):

    sio = io.StringIO(unicode(
        data.read(), errors='ignore'
    ), newline=None)

    reader = csv.DictReader(sio, dialect='excel')

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

