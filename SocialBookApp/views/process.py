'''
Created on 20-JAN-2021

@author: Abishek Rajagopal
'''


from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet, ViewSet
from SocialBookApp.models.bookmodels import (Book)
from SocialBookApp.models.usermodels import (App_User)
from SocialBookApp.serializers.serializers import (BookSerializer,App_UserSerializer)
from rest_framework.response import Response
import logging
import json

logger = logging.getLogger("book.request")

class LoginCheckSet(ModelViewSet):

    queryset = App_User.objects.all()
    serializer_class = App_UserSerializer


    def login(self, request):
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')
            try:
                item = App_User.objects.get(username=username)
                logger.info(item.password)
                if (item.password == password):
                    return Response("User Verification Successful", status=200)
                else:
                    return Response("Username or Password MisMatch", status=404)


            except App_User.DoesNotExist:
                return Response("Username does not Exist. Please Register", status=404)

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=404)



