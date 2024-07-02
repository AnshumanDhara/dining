from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    
    def __str__(self):
        return self.username
    
class Place(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    phone_no = models.IntegerField()
    website = models.URLField(max_length=200)
    open_time = models.DateTimeField(null=False)
    close_time = models.DateTimeField(null=False)
    
    def __str__(self):
        return self.name