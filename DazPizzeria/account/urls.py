from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from . import views


app_name = 'account'

urlpatterns = [
        path('index/', views.IndexView.as_view(), name='index'),
        path('signup/', views.SignUpView.as_view(), name='signup'),
        path('login/', LoginView.as_view(template_name='account/login.html'), name='login'),
        path('logout/', LogoutView.as_view(), name='logout'),
        path('orders/', include('orders.urls', namespace='orders')),
]
