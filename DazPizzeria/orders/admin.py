from django.contrib import admin
from .models import ItemType, Order, OrderItem, Menu, Topping

# Register your models here.

admin.site.register(Menu)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ItemType)
admin.site.register(Topping)
