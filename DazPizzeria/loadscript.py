print("===============================================================")
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pizza.settings')

import django
django.setup()
import pandas as pd

#Import django models to added from django. Alternatively we can use Postgres python API to load data.
from orders.models import Menu, ItemType, Topping


def add_Item():
    choices = ['Regular Pizza', 'Sicilian Pizza', 'Salads', 'Subs', 'Pasta', 'Dinner Platters']
    for i in choices:
        print(i)
        item = ItemType.objects.get_or_create(itemType=i)
# id  Type
# 1   'Regular Pizza'
# 2   'Sicilian Pizza'
# 3   'Salads'
# 4   'Subs'
# 5   'Pasta'
# 6   'Dinner Platters'


#Read excel file with menu table
cwd = os.path.dirname(os.path.abspath(__file__))
menu = os.path.join(cwd,'menulist.xlsx')

menudf = pd.read_excel(menu)
def add_menu():
    for i, j in menudf.iterrows():
        # i-sheetname j-table header
        reg = ItemType.objects.get(itemType=j['type_id'])
        Menu.objects.create(type =reg, item=j['item'], size=j['size'], price=j['price'])


def add_toppings():
    toppings = ['Pepperoni',
                'Sausage',
                'Mushrooms',
                'Onions',
                'Ham',
                'Canadian Bacon',
                'Pineapple',
                'Eggplant',
                'Tomato & Basil',
                'Green Peppers',
                'Hamburger',
                'Spinach',
                'Artichoke',
                'Buffalo Chicken',
                'Barbecue Chicken',
                'Anchovies',
                'Black Olives',
                'Fresh Garlic',
                'Zucchini',
                ]
    for i in toppings:
        top = Topping.objects.get_or_create(topping=i)
        print(i)
    print("Toppings population done!")


if __name__ == '__main__':
    print("populating script!")
    add_toppings()
    add_Item()
    add_menu()
    print("population complete!")
