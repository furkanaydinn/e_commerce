from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User,related_name='userprofile',on_delete=models.CASCADE)
    phone = models.CharField(blank=True, max_length=20)
    address = models.CharField(blank=True, max_length=150)
    city = models.CharField(blank=True, max_length=20)
    country = models.CharField(blank=True, max_length=50)

    def __str__(self):
        return self.user.username

    def user_name(self):
        return self.user.first_name + ' '  + self.user.last_name + ' [' + self.user.username + '] '