from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import HomePageView



urlpatterns = [
    path('', HomePageView.as_view(), name='home')
] + static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0] )

1
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)