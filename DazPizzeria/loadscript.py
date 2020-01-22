print("===============================================================")
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pizza.settings')

import django
django.setup()

##Fake pop script
import random
from orders.models import Menu, ItemType, Topping


def add_Item():
    choices = ['Regular Pizza', 'Sicilian Pizza', 'Salads', 'Subs', 'Pasta', 'Dinner Platters']
    for i in choices:
        print(i)
        item = ItemType.objects.get_or_create(itemType=i)

def add_menu():
    choices = ({'Item': 'Cheese', 'Size':'Small', 'Price':12.70},{'Item': 'Special', 'Size':'Small', 'Price':30.45},{'Item': 'Garden Salad', 'Size':'Regular', 'Price':9.75},)
    item = ItemType.objects.all()
    ind = 0
    for i in item:
        #print(i.pk)
        menu = Menu.objects.get_or_create(type_id=i, item=choices[ind]['Item'], size=choices[ind]['Size'],price=choices[ind]['Price'],)
        ind +=1

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

# topics = ['Search', 'Social', 'Marketplace', 'News', 'Games']
#
# def add_topic():
#     t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
#     t.save()
#
#     return t
#
# def populate(N=5):
#
#     for entry in range(N):
#
#         #get the topic for the entry
#         top = add_topic()
#
#         #create the fake data for entry
#         fake_url = fakegen.url()
#         fake_date = fakegen.date()
#         fake_name = fakegen.company()
#
#         webpg = Webpage.objects.get_or_create(topic=top, url = fake_url, name=fake_name)[0]
#
#         #create a fake access record for that webpage
#
#         acc_rec = AccessRecord.objects.get_or_create(name=webpg, date=fake_date)[0]

if __name__ == '__main__':
    print("populating script!")
    add_toppings()
    #add_Item()
    #add_menu()
    print("population complete!")
