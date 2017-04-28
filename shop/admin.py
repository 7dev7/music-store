from django.contrib import admin

from shop.models import BasicProductType, ProductType, Product, CartItem, Order

admin.site.register([BasicProductType, Product, ProductType, CartItem, Order])
