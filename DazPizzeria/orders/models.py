from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from account.models import Profile
from django.conf import settings

# Create your models here.



class ItemType(models.Model):
    id = models.AutoField(primary_key=True)
    itemType = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.itemType


class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.ForeignKey('orders.ItemType', to_field='itemType', on_delete=models.CASCADE)
    item = models.CharField(max_length=30)
    size = models.CharField(max_length=30)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return "%s, %s, %s, %s" %(self.type, self.item, self.size, self.price)


class Order(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    cart = models.CharField(max_length=30, default='Open')
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.user_id.username

class Topping(models.Model):
    topping = models.CharField(max_length=30)

    def __str__(self):
        return self.topping

class OrderItem(models.Model):


    id = models.AutoField(primary_key=True)
    order_id = models.ForeignKey('orders.Order', on_delete=models.CASCADE)
    menu_id = models.ForeignKey('orders.Menu', related_name='menus' ,on_delete=models.CASCADE)
    quantity = models.IntegerField()
    status = models.CharField(max_length=30)
    topping = models.CharField(max_length=120, default='')

    def __str__(self):
        return "{}, {}".format(self.menu_id.type, self.menu_id.item)
