from django.views.generic import TemplateView

#Write your views here

class TestView(TemplateView):
    template_name = 'test.html'

class ThanksView(TemplateView):
    template_name = 'thanks.html'

class IndexView(TemplateView):
    template_name = 'welcome.html'

class HomeView(TemplateView):
    template_name = 'homepage.html'
