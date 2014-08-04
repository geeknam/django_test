from django.db import models


class Customer(models.Model):

    full_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __unicode__(self):
        return '%s <%s>' % (self.full_name, self.email)


class Product(models.Model):

    code = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return '%s <%s>' % (self.name, self.code)


class Order(models.Model):

    order_code = models.CharField(max_length=100, unique=True)
    address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    postcode = models.CharField(max_length=10)

    customer = models.ForeignKey(Customer, related_name='orders')
    

    def __unicode__(self):
        return self.order_code


class OrderItem(models.Model):

    order = models.ForeignKey(Order, related_name='items')
    product = models.ForeignKey(Product)
    quantity = models.IntegerField()