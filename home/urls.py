from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import HomePageView, login_view, signup_view



urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('login/', login_view, name='login'),
    path('signup/', signup_view, name='signup'),
] 



