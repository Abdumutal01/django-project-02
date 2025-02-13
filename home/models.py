from django.db import models

# Create your models here.

class Venue(models.Model):
    venue_image = models.ImageField(null=True, blank=True, upload_to='venues/')
