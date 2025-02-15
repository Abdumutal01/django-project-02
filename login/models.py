from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.


class User(models.Model):
    login = models.CharField
    password = models.CharField
    
    
    def check_password(self, raw_password):
        return check_password(raw_password, self.password)