from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from config import settings 
from django.contrib.auth import authenticate
from django.contrib import messages
from .models import User

# Create your views here.

def home(request):
    return render(request, 'home.html'), {"MEDIA_URL": settings.MEDIA_URL}


class HomePageView(TemplateView):
    template_name = 'home.html'


def login_view(request):
    if request.method == "POST":
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            username(request, user)
            print('End')
            return redirect('home')
        elif not user:
            messages.error(request, "Foydalanuvchi topilmadi ro'yhatdan o'ting ")
            return redirect('signup')
        else:
            print('again')
            messages.error(request, "Foydalanuvchi nomi yoki parol noto'g'ri  ")
            return redirect('login')
    return render(request, 'login.html')



def signup_view(request):
    return render(request, 'signup.html')