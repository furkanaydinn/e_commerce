from django.db import models

# Create your models here.

class Team(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    job = models.CharField(max_length = 30)
    image = models.ImageField(upload_to = 'team_images/',blank=True,null=True)


    def __str__(self):
        return self.name


class Clients(models.Model):
    client_name = models.CharField(max_length=30)
    image = models.ImageField(upload_to = 'client_images/',blank=True,null=True)

    def __str__(self):
        return self.client_name


class Contact(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField(max_length=254)
    message = models.TextField()

    def __str__(self):
        return self.name
