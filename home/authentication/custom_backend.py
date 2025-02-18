# your_project/your_app/authentication/custom_backend.py
from django.contrib.auth.models import User
from django.contrib.auth.backends import BaseBackend

class CustomBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None
