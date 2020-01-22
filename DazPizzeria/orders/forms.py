from django import forms
from .models import Order, Menu, ItemType, OrderItem, Topping

#form to take orders

class TypeForm(forms.Form):
    typeChoices = [('Regular Pizza', 'Regular Pizza'),
                    ('Sicilian Pizza', 'Sicilian Pizza'),
                    ('Subs', 'Subs'), ('Pasta','Pasta'),
                    ('Salads', 'Salads'),
                    ('Dinner Platters', 'Dinner Platters')]
    type = forms.ChoiceField(choices=typeChoices, initial=0)

class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderItem
        fields = ['menu_id', 'quantity']

class ToppingForm(forms.Form):
    toppings = list(Topping.objects.all())
    choice = [[str(object),str(object)] for object in toppings]

    topping = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple(), choices=choice)
