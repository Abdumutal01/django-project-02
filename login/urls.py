from django.contrib import admin
from django.urls import path, include
from .views import login_view, LogInPageView

urlpatterns = [
    # path('login/', LogInPageView.as_view , name='login' ),
    path('', login_view, name='login')
]