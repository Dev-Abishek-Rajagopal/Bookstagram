'''
Created on 20-JAN-2021

@author: Abishek Rajagopal
'''

from django.contrib.auth.models import User
from djongo import models
from django.conf import settings
from fernet_fields import EncryptedTextField
from unixtimestampfield.fields import UnixTimeStampField
from django.contrib.auth.models import AbstractUser





class App_User(models.Model):

    user = models.ForeignKey(User, related_name='App_User',on_delete=models.CASCADE)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    username = models.CharField(max_length=200,unique=True)
    usertype = models.CharField(max_length=200)
    password = EncryptedTextField(max_length=600)
    country = models.CharField(max_length=200)
    email = models.CharField(max_length=200,unique=True)
    active = models.BooleanField(default=False)
    contact =  models.CharField(max_length=200,null=True)
    friends = models.IntegerField(default=0)
    wallet = models.IntegerField(default=500)
    dp = models.TextField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.username = self.username.lower()
        self.email = self.email.lower()

        return super(App_User, self).save(*args, **kwargs)

class friendlist(models.Model):
    user = models.ForeignKey(App_User, on_delete=models.CASCADE,related_name='friendlistyou')
    friend = models.ForeignKey(App_User, on_delete=models.CASCADE,related_name='friendlistfriend')
    relationship = models.CharField(max_length=200)

class profileComment(models.Model):
    user = models.ForeignKey(App_User, on_delete=models.CASCADE,related_name='profileCommentyou')
    chatter = models.ForeignKey(App_User, on_delete=models.CASCADE,related_name='profileCommentfriend')
    comments = models.TextField()
    publist = UnixTimeStampField(auto_now=True,null=True,editable=True)
    likes = models.IntegerField(default=0)




