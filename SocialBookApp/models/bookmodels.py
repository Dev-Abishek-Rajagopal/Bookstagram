'''
Created on 20-JAN-2021

@author: Abishek Rajagopal
'''


from djongo import models
from django.conf import settings
from unixtimestampfield.fields import UnixTimeStampField
from SocialBookApp.models.usermodels import (App_User)
# from SocialBookApp.models.bookmodels import (BookUserTree)
from treenode.models import TreeNodeModel

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
    ratings = models.FloatField(default=5)
    publist = UnixTimeStampField(auto_now=True, null=True,editable=False)



class OwnBook(models.Model):
    Book = models.ForeignKey(Book, on_delete=models.CASCADE, )
    user = models.ForeignKey(App_User, on_delete=models.CASCADE,related_name='Buyer')
    Own = models.CharField(max_length=200)
    referrer = models.ForeignKey(App_User, on_delete=models.CASCADE,related_name='referrer')
    publist = UnixTimeStampField(auto_now=True, null=True,editable=False)

class BookWishlist(models.Model):
    Book = models.ForeignKey(Book, on_delete=models.CASCADE, )
    user = models.ForeignKey(App_User, on_delete=models.CASCADE)
    publist = UnixTimeStampField(auto_now=True, null=True)

class BookTreeDB(models.Model):
    Book = models.ForeignKey(Book, on_delete=models.CASCADE, )
    Tree = models.IntegerField(default=0)

class BookTreeConnect(models.Model):
    Book = models.ForeignKey(Book, on_delete=models.CASCADE, )
    Tree = models.IntegerField(default=0)

class BookNewsFeed(models.Model):

    Author = models.ForeignKey(App_User, on_delete=models.CASCADE,related_name='youself')
    Buyer = models.ForeignKey(App_User, on_delete=models.CASCADE,related_name='bookBuyer')
    referrer = models.ForeignKey(App_User, on_delete=models.CASCADE, related_name='feedreferrer')
    Book = models.ForeignKey(Book, on_delete=models.CASCADE, )
    comments = models.TextField()
    publist = UnixTimeStampField(auto_now=True,null=True)

class FriendNewsFeed(models.Model):

    user = models.ForeignKey(App_User, on_delete=models.CASCADE,related_name='friendyou')
    friend = models.ForeignKey(App_User, on_delete=models.CASCADE,related_name='friendfriend')
    comments = models.TextField()
    publist = UnixTimeStampField(auto_now=True,null=True)

class CommentsNewsFeed(models.Model):

    user = models.ForeignKey(App_User, on_delete=models.CASCADE,related_name='commentyou')
    Author = models.ForeignKey(App_User, on_delete=models.CASCADE, related_name='Auth')
    Book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book')
    Bookcomments = models.ForeignKey(BookComments, on_delete=models.CASCADE)
    comments = models.TextField()
    publist = UnixTimeStampField(auto_now=True,null=True)

class BookUserTree(TreeNodeModel):

    # the field used to display the model instance
    # default value 'pk'
    treenode_display_field = 'UserName'
    #
    # name = models.CharField(max_length=50)

    Book = models.ForeignKey(Book, on_delete=models.CASCADE, )
    user = models.ForeignKey(App_User, on_delete=models.CASCADE)
    UserName = models.CharField(max_length=200)

    class Meta(TreeNodeModel.Meta):
        verbose_name = 'BookUserTree'
        verbose_name_plural = 'BookUserTrees'

    def save(self, *args, **kwargs):
        list = App_User.objects.get(id=self.user.id)
        self.UserName = list.username
        return super(BookUserTree, self).save(*args, **kwargs)