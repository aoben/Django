from django.urls import path

from . import views

app_name = 'orders'

urlpatterns = [
    path("", views.index, name="index"),
    path("menu/", views.MenuView.as_view(), name="menu"),
    path("cart/", views.CartView.as_view(), name="cart"),
    path("order/<int:pk>/", views.OrderDetailView.as_view(), name="orderdetail"),
    path("placeorder/", views.PlaceOrderView, name="placeorder"),
    path("topping/<int:pk>/", views.ToppingView.as_view(), name="topping"),
    path("continue/", views.ContinueView.as_view(), name="continue"),
]
