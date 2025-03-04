from django.db import models
from django.contrib.auth.models import User


# Create your models here.



class Contact(models.Model):
    
    listing = models.CharField(max_length=200)
    listing_id = models.IntegerField()
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(auto_now_add=True)
    user_id = models.IntegerField(blank=True)

    class SiteConfigurationConfig:
        default_auto_field = 'django.db.models.AutoField'
    
    def __str__(self):
        return self.name
