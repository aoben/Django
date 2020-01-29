from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, TemplateView, CreateView, FormView, UpdateView
from .models import Menu, Order, OrderItem, ItemType, Topping
from .forms import OrderForm, TypeForm, ToppingForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model



# Create your views here.
def index(request):
    return render(request, 'orders/index.html')



###Register and Login views




class MenuView(ListView):
    queryset = Menu.objects.all()
    template_name = 'orders/menu.html'

    def get_context_data(self, **kwargs):
        context = super(MenuView, self).get_context_data(**kwargs)
        context['regulartype'] = Menu.objects.filter(type='Regular Pizza')
        context['siciliantype'] = Menu.objects.filter(type="Sicilian Pizza")
        context['subs'] = Menu.objects.filter(type="Subs")
        context['pasta'] = Menu.objects.filter(type="Pasta")
        context['salads'] = Menu.objects.filter(type="Salads")
        context['dinner_platters'] = Menu.objects.filter(type="Dinner Platters")
        context['topping'] = Topping.objects.all()
        return context

class ContinueView(LoginRequiredMixin, TemplateView):
    template_name = 'orders/continue.html'
    success_url = 'continue'
    # form_class = ToppingForm


class ToppingView(LoginRequiredMixin, FormView):
    form_class = ToppingForm
    template_name = 'orders/toppings.html'
    success_url = reverse_lazy('orders:continue')

    def get_context_data(self, **kwargs):
        context = super(ToppingView, self).get_context_data(**kwargs)
        context['objects'] = OrderItem.objects.filter(id=self.kwargs.get('pk'))
        return context


    def form_valid(self, form):
        data = list(form.cleaned_data["topping"])
        orderitem = OrderItem.objects.get(id=self.kwargs.get('pk'))
        orderitem.topping = data
        orderitem.save()
        return super().form_valid(form)


#View for placing orders

@login_required
def PlaceOrderView(request):
    print(request.user.username)
    #render forms
    if request.method == "POST":
        #if the form used is TypeForm
        if 'typeform' in request.POST:
            #print(request.POST)

            form = TypeForm(request.POST)

            if form.is_valid:

                form_value = request.POST.copy()
                typeValue = form_value.get('type')
                valueset = Menu.objects.filter(type=typeValue)

                form = OrderForm
                context = {'valueset':valueset, 'typeValue':typeValue, 'form':form}

        #If the form used is OrderForm
        else:
            print(request.POST)
            #save info into Tables then redirect user to cart
            form = request.POST
            if form:
                form_value = request.POST.copy()
                user = request.user
                #print(user)

                order = Order.objects.filter(user_id=user, cart='Open')
                #check if queryset exists, if not add new record
                if not order.exists():
                    order = Order(user_id=user, cart='Open')
                    order.save()
                    order = Order.objects.filter(user_id=user, cart='Open')

                menu = Menu.objects.get(id=form_value.get('menuitem'))
                orderitem = OrderItem(order_id = order[0],
                                        menu_id = menu,
                                        quantity = form_value.get('quantity'),
                                        status = 'Pending')
                orderitem.save()
                print(orderitem.pk)
                type = str(orderitem.menu_id.type)
                #print(type)

                if type in ['Regular Pizza', 'Sicilian Pizza']:
                    #Redirect to Toppings Page
                    return redirect(reverse('orders:topping', kwargs={'pk':orderitem.pk}))

                #else Redirect to Continue page
                else:
                    return redirect(reverse('orders:continue'))
    else:
        form = TypeForm
        context = {'form':form}
    return render(request, 'orders/placeorder.html', context)




class CartView(ListView):
    queryset = OrderItem.objects.all()
    template_name = 'orders/cart.html'

    def get_context_data(self, **kwargs):
        context = super(CartView, self).get_context_data(**kwargs)
        context['cx_order'] = OrderItem.objects.filter(order_id__user_id__username=self.request.user)
        return context

class OrderDetailView(DetailView):
    model = Order
    template_name = 'orders/orderdetail.html'
