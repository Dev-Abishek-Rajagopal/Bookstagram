'''
Created on 20-JAN-2021

@author: Abishek Rajagopal
'''



import json
import logging

from rest_framework import serializers

from SocialBookApp.models.bookmodels import (Book)
from SocialBookApp.models.usermodels import (App_User)
from rest_framework.response import Response

logger = logging.getLogger("book.request")

class BookSerializer(serializers.ModelSerializer):


    class Meta:
        model = Book;
        fields = ('name', 'authname', 'rate', 'likes', 'share','views');

    def create(self, validated_data):
        try:
            return Book.objects.create(**validated_data);

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))


    def update(self, instance, validated_data):
        try:
            instance.id = validated_data.get('id', instance.id);
            instance.name = validated_data.get('name', instance.name);
            instance.authname_id = validated_data.get('authname', instance.authname);
            # instance.publist = validated_data.get('publist', instance.publist);
            instance.rate = validated_data.get('rate', instance.rate);
            instance.likes = validated_data.get('likes', instance.likes);
            instance.share = validated_data.get('share', instance.share);
            instance.views = validated_data.get('rate', instance.views);
            instance.save();
            return instance;

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))



class App_UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = App_User;
        fields = ('username', 'usertype', 'password', 'country','mailid',"contact",'friends','wallet');

    def create(self, validated_data):
        try:
            return App_User.objects.create(**validated_data);

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))


    def update(self, instance, validated_data):
        try:
            instance.username = validated_data.get('username', instance.username);
            instance.usertype = validated_data.get('usertype', instance.usertype);
            instance.password = validated_data.get('password', instance.password);

            instance.country = validated_data.get('country', instance.country);
            instance.mailid = validated_data.get('mailid', instance.mailid);
            instance.contact = validated_data.get('contact', instance.contact);
            instance.friends = validated_data.get('friends', instance.friends);
            instance.wallet = validated_data.get('wallet', instance.wallet);
            instance.save();
            return instance;

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
