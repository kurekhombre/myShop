from django.contrib.auth.models import User
from django.db import models

from product.models import Product


class Order(models.Model):

    ORDERED = 'ordered'
    SHIPPED = 'shipped'
    STATUS_CHOICES = (
        (ORDERED, 'Ordered'),
        (SHIPPED, 'Shipped')
    )

    user = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE, blank=True, null=True)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField(max_length=250)
    address = models.CharField(max_length=250)
    zipcode = models.CharField(max_length=250)
    place = models.CharField(max_length=250)
    phone = models.CharField(max_length=250)

    created_at = models.DateTimeField(auto_now_add=True)

    paid = models.BooleanField(default=False)
    paid_amount = models.IntegerField(blank=True, null=True)

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default=ORDERED)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='items', on_delete=models.CASCADE)
    price = models.IntegerField(blank=True, null=True)
    quantity = models.IntegerField(default=1)

