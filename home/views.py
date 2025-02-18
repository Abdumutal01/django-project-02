from django.shortcuts import render, redirect
from django.views.generic import TemplateView

from config import settings 
from django.contrib.auth import authenticate, login as auth_login

from django.contrib import messages
from django.contrib.auth.models import User
from .models import User as HomeUser
from .forms import CustomUserCreationForm
# from .forms import UserCreationForm


# Create your views here.

def home(request):
    return render(request, 'home.html'), {"MEDIA_URL": settings.MEDIA_URL}


class HomePageView(TemplateView):
    template_name = 'home.html'


class LoginView(TemplateView):
    template_name = 'login.html'

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print("Foydalanuvchi nomi:", username, "Parol:", password)

        # authenticate ni ishlatish
        user = authenticate(request, username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return redirect('home')  # home URL nomiga to'g'ri kelishini tekshirib ko'ring
        else:
            messages.error(request, "Foydalanuvchi nomi yoki parol noto'g'ri")
            return redirect('login')

    return render(request, 'login.html')

def signup_view(request):
    print(request)
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        print(form)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Ro‘yxatdan o‘tishda xatolik bor")
        
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {"form": form})