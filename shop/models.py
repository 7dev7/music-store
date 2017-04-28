from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.db import models


class BasicProductType(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class ProductType(models.Model):
    name = models.CharField(max_length=255, unique=True)
    internal_name = models.CharField(max_length=255)
    basic_type = models.ForeignKey(BasicProductType)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    description = models.TextField()
    amount = models.IntegerField()
    type = models.ForeignKey(ProductType)
    img = models.ImageField(null=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    order_date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User)
    total = models.DecimalField(decimal_places=2, max_digits=10)


class CartItem(models.Model):
    owner = models.ForeignKey(User)
    product = models.ForeignKey(Product)
    quantity = models.IntegerField(default=1)
    is_active = models.BooleanField(default=True)

    order = models.ForeignKey(Order, null=True)
