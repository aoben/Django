from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.shortcuts import redirect
from django.views.generic import CreateView, TemplateView
from .forms import SignUpForm, LogInForm
from .models import Profile

# Create your views here.

class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'account/signup.html'


class IndexView(TemplateView):
    template_name = 'account/index.html'
