from django.db import models

# Create your models here.


class userModel(models.Model):
    fullName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.BigIntegerField()
    company_name = models.CharField(max_length=50)
    message = models.CharField(max_length=250)
    
    