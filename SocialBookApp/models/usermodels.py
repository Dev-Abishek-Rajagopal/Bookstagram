'''
Created on 20-JAN-2021

@author: Abishek Rajagopal
'''


from djongo import models
from django.conf import settings
from fernet_fields import EncryptedTextField

class App_User(models.Model):

    username = models.CharField(max_length=200,default="user")
    usertype = models.CharField(max_length=200,default="both")
    password = EncryptedTextField(max_length=600,default="*")
    country = models.CharField(max_length=200,default="Canada")
    mailid = models.CharField(max_length=200,null=True)
    contact =  models.CharField(max_length=200,null=True)
    friends = models.IntegerField(default=0)
    wallet = models.IntegerField(default=500)


class friendlist(models.Model):
    you = models.ForeignKey(App_User, on_delete=models.CASCADE,related_name='friendlistyou')
    friend = models.ForeignKey(App_User, on_delete=models.CASCADE,related_name='friendlistfriend')
    relationship = models.CharField(max_length=200,default="addfriend")

class profileComment(models.Model):
    you = models.ForeignKey(App_User, on_delete=models.CASCADE,related_name='profileCommentyou')
    friend = models.ForeignKey(App_User, on_delete=models.CASCADE,related_name='profileCommentfriend')
    comments = models.TextField()