from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

# Create your views here.

def login_view(request):
    if request.method == "POST":
        
        login = request.POST.get('login')
        password = request.POST.get('password')
        
        user = authenticate(request, login=login, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Foydalanuvchi nomi yoki parol noto'g'ri ")
    return render(request, 'logIn.html')
