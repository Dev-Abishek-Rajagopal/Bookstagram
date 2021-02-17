'''
Created on 20-JAN-2021

@author: Abishek Rajagopal
'''



import json
import logging

from rest_framework import serializers

from SocialBookApp.models.bookmodels import (Book)
from SocialBookApp.models.usermodels import (App_User,friendlist,profileComment,profileTXTPost,TXTPostComments,profileTXTPost)
from django.contrib.auth.models import User
from rest_framework.response import Response

logger = logging.getLogger("book.request")

class BookSerializer(serializers.ModelSerializer):


    class Meta:
        model = Book;
        fields = ("id", 'name', 'authname', 'rate', 'stars', 'share','views','booktype');

    def create(self, validated_data):
        try:
            return Book.objects.create(**validated_data);

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))


    def update(self, instance, validated_data):
        try:
            logger.info("hi")
            instance.id = validated_data.get('id', instance.id);
            instance.name = validated_data.get('name', instance.name);
            instance.authname_id = validated_data.get('authname', instance.authname);
            # instance.publist = validated_data.get('publist', instance.publist);
            instance.rate = validated_data.get('rate', instance.rate);
            instance.stars = validated_data.get('stars', instance.stars);
            instance.share = validated_data.get('share', instance.share);
            instance.views = validated_data.get('rate', instance.views);
            instance.save();
            return instance;

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))

class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = User;
        fields = ("id",'username','first_name', 'last_name', 'email',"password")

    def create(self, validated_data):
        try:
            return User.objects.create(**validated_data);

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))


    def update(self, instance, validated_data):
        try:
            instance.id = validated_data.get('id', instance.id);
            instance.first_name = validated_data.get('first_name', instance.first_name);
            instance.last_name = validated_data.get('last_name', instance.last_name);
            instance.password = validated_data.get('password', instance.password);
            instance.email = validated_data.get('email', instance.email);
            # instance.username = validated_data.get('username', instance.username);
            instance.save();
            return instance;

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))


class App_UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = App_User;
        fields = ('id','user','first_name', 'active', 'last_name','username', 'usertype', 'password', 'country','email',"contact",'friends','wallet');

    def create(self, validated_data):
        try:
            return App_User.objects.create(**validated_data);

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))


    def update(self, instance, validated_data):
        try:
            instance.id = validated_data.get('id', instance.id);
            instance.first_name = validated_data.get('first_name', instance.first_name);
            instance.last_name = validated_data.get('last_name', instance.last_name);
            instance.username = validated_data.get('username', instance.username);
            instance.usertype = validated_data.get('usertype', instance.usertype);
            instance.password = validated_data.get('password', instance.password);
            instance.country = validated_data.get('country', instance.country);
            instance.email = validated_data.get('email', instance.email);
            instance.contact = validated_data.get('contact', instance.contact);
            instance.friends = validated_data.get('friends', instance.friends);
            instance.wallet = validated_data.get('wallet', instance.wallet);
            instance.save();
            return instance;

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))

class App_UserSerializerI(serializers.ModelSerializer):


    class Meta:
        model = App_User;
        fields = ('id','first_name', 'last_name','username', 'usertype', 'country','email',"contact",'friends');

    def create(self, validated_data):
        try:
            return App_User.objects.create(**validated_data);

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))





class friendlistSerializer(serializers.ModelSerializer):


    class Meta:
        model = friendlist;
        fields = ('id','user','friend', "relationship");

    def create(self, validated_data):
        try:
            return friendlist.objects.create(**validated_data);

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))

    def update(self, instance, validated_data):
        try:
            logger.info(validated_data)
            instance.id = validated_data.get('id', instance.id);
            instance.user_id = validated_data.get('user', instance.user);
            instance.friend_id = validated_data.get('friend', instance.friend);
            instance.relationship = validated_data.get('relationship', instance.relationship);
            instance.save();
            return instance;

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))


class profileTXTPostSerializer(serializers.ModelSerializer):


    class Meta:
        model = profileTXTPost;
        fields = ('id','user','post','comments', "likes","share","publist");

    def create(self, validated_data):
        try:
            return profileTXTPost.objects.create(**validated_data);

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))


class profileTXTPostSerializerI(serializers.ModelSerializer):


    class Meta:
        model = profileTXTPost;
        fields = ('id','user','post','comments', "likes","share");

    def create(self, validated_data):
        try:
            return profileTXTPost.objects.create(**validated_data);

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))

    def update(self, instance, validated_data):
        try:

            logger.info(validated_data.get('likes', instance.likes))
            instance.id = validated_data.get('id', instance.id);
            instance.user_id = validated_data.get('user', instance.user);
            instance.post = validated_data.get('post', instance.post);
            instance.comments = validated_data.get('comments', instance.comments);
            instance.likes = validated_data.get('likes', instance.likes);
            instance.share = validated_data.get('share', instance.share);
            instance.save();
            return instance;

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))


class TXTPostCommentsSerializer(serializers.ModelSerializer):


    class Meta:
        model = TXTPostComments;
        fields = ('id','user','post','comments', "likes");

    def create(self, validated_data):
        try:
            return TXTPostComments.objects.create(**validated_data);

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))

    def update(self, instance, validated_data):
        try:

            instance.id = validated_data.get('id', instance.id);
            instance.user_id = validated_data.get('user', instance.user);
            instance.post_id = validated_data.get('post', instance.post);
            instance.comments = validated_data.get('comments', instance.comments);
            instance.likes = validated_data.get('likes', instance.likes);
            instance.save();
            return instance;

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))