from django.db import models
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

class Venue(models.Model):
    venue_image = models.ImageField(null=True, blank=True, upload_to='venues/')


class UserManager(BaseUserManager):
    def create_user(self, username, password=None):
        if not username:
            raise  ValueError("Foydalanuvchi topilmadi")
        
        user = self.model(username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, username, password=None):
        user = self.create_user(username, password)
        user.is_admin = True
        user.save(using=self._db)
        return user
        


class User(AbstractBaseUser):
    username = models.CharField(max_length=250, unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    objects = UserManager()
    
    USERNAME_FIELD = "login"