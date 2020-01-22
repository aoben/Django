print("===============================================================")
import os
import xlrd
import pandas as pd
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pizza.settings')

import django
django.setup()

from orders.models import Menu, ItemType
cwd = os.path.dirname(os.path.abspath(__file__))
menu = os.path.join(cwd,'menu.xlsx')

menudf = pd.read_excel(menu)

def add_menu():
    for i, j in menudf.iterrows():
        reg = ItemType.objects.get(itemType="Regular Pizza")
        Menu.objects.get_or_create(type = reg, item=j['item'], size=j['size'], price=j['price'])




if __name__ == '__main__':
    print("populating script!")
    add_menu()
    print("population complete!")
