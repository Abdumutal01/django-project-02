from django.shortcuts import render
from django.views.generic import TemplateView
from config import settings 
# Create your views here.

def home(request):
    return render(request, 'home.html'), {"MEDIA_URL": settings.MEDIA_URL}


class HomePageView(TemplateView):
    template_name = 'home.html'
