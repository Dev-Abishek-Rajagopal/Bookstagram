'''
Created on 20-JAN-2021

@author: Abishek Rajagopal
'''


from djongo import models
from django.conf import settings
from unixtimestampfield.fields import UnixTimeStampField
from SocialBookApp.models.usermodels import (App_User)

# Create your models here.
class Book(models.Model):
    name = models.CharField(max_length=200,default="BookName")
    authname = models.ForeignKey(App_User, on_delete=models.CASCADE)
    publist = UnixTimeStampField(auto_now=True,null=True)
    booktype =  models.CharField(max_length=200,default="Text")
    rate = models.FloatField(default=0.0)
    stars = models.IntegerField(default=0)
    share = models.IntegerField(default=0)
    views = models.IntegerField(default=0)
    dp = models.CharField(max_length=200, default="")
    desc = models.CharField(max_length=500, default="")
    # dp = models.ImageField(upload_to ='bookDP/',default="0")

class TextBook(models.Model):
    Book = models.ForeignKey(Book, on_delete=models.CASCADE,)
    content = models.TextField()
    type = models.CharField(max_length=200)
    publist = UnixTimeStampField(auto_now=True, null=True)

class BookComments(models.Model):
    Book = models.ForeignKey(Book, on_delete=models.CASCADE, )
    user = models.ForeignKey(App_User, on_delete=models.CASCADE)
    comments = models.TextField()
    publist = UnixTimeStampField(auto_now=True, null=True,editable=False)

class OwnBook(models.Model):
    Book = models.ForeignKey(Book, on_delete=models.CASCADE, )
    user = models.ForeignKey(App_User, on_delete=models.CASCADE)
    Own = models.CharField(max_length=200)
    publist = UnixTimeStampField(auto_now=True, null=True,editable=False)

class BookWishlist(models.Model):
    Book = models.ForeignKey(Book, on_delete=models.CASCADE, )
    user = models.ForeignKey(App_User, on_delete=models.CASCADE)
    publist = UnixTimeStampField(auto_now=True, null=True)