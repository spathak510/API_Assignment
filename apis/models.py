from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=255,null=True,blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)









class Contacts(models.Model):
    user = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    name = models.CharField(max_length=255,null=True,blank=True)
    email = models.CharField(max_length=255,null=True,blank=True)
    phone = models.CharField(max_length=255,null=True,blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255,null=True,blank=True)

