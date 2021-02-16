'''
Created on 20-JAN-2021

@author: Abishek Rajagopal
'''


from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from SocialBookApp.models.bookmodels import (Book)
from SocialBookApp.models.usermodels import (App_User)
from django.contrib.auth.models import User
from SocialBookApp.serializers.serializers import (BookSerializer,App_UserSerializer,UserSerializer)
from rest_framework.response import Response
import logging
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
import json
from verify_email.email_handler import send_verification_email
from rest_framework.authtoken.models import (Token)
from SocialBookApp.views.process import (smtpsender)
from django.shortcuts import redirect
from rest_framework.permissions import AllowAny

logger = logging.getLogger("book.request")

class BookVeiwSet(ModelViewSet):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


    def list_Book(self, request):
        try:
            book_list = Book.objects.all()
            serializer = BookSerializer(book_list, many=True)
            # logger.info("hi")
            # for i in serializer.data:
            #     image_data =""
            #     with open(i['dp'], "rb") as image_file:
            #         image_data = base64.b64encode(image_file.read()).decode('utf-8')
            #     i['dp']= image_data
            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)


    def create_Book(self, request):
        try:
            serializer = BookSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def get_Book(self, request,*args, **kwargs):
        try:
            pk = self.kwargs['pk']
            list = Book.objects.get(id=pk)
            serializer = BookSerializer(list)
            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def delete_Book(self, request,*args, **kwargs):
        try:
            pk = self.kwargs['pk']
            item = Book.objects.get(id=pk)
            item.delete()
            return Response(json.loads('{"response" : "Book deleted successfully."}'), status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def update_Book(self, request, *args, **kwargs):
        try:
            serializer = BookSerializer(data=request.data)
            pk = self.kwargs['pk']
            item = Book.objects.get(id=pk)
            if serializer.is_valid():
                serializer.update(item, serializer.data)
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=200)

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

class UserVeiwSet(ModelViewSet):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = App_User.objects.all()
    serializer_class = App_UserSerializer


    def list_User(self, request):
        try:
            App_User_list = App_User.objects.all()
            serializer = App_UserSerializer(App_User_list, many=True)
            # logger.info("hi")
            # for i in serializer.data:
            #     image_data =""
            #     with open(i['dp'], "rb") as image_file:
            #         image_data = base64.b64encode(image_file.read()).decode('utf-8')
            #     i['dp']= image_data
            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)



    def get_User(self, request,*args, **kwargs):
        try:
            pk = self.kwargs['pk']
            list = App_User.objects.get(id=pk)
            serializer = App_UserSerializer(list)
            auth = Token.objects.get(user=pk)
            datas = serializer.data.copy()
            datas["token"] = auth.key
            logger.info(auth.key)
            return Response(datas, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def delete_User(self, request,*args, **kwargs):
        try:
            pk = self.kwargs['pk']
            item = App_User.objects.get(id=pk)
            item.delete()
            return Response(json.loads('{"response" : "Book deleted successfully."}'), status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def update_User(self, request, *args, **kwargs):
        try:
            serializer = App_UserSerializer(data=request.data)
            pk = self.kwargs['pk']
            item = App_User.objects.get(id=pk)
            if serializer.is_valid():
                serializer.update(item, serializer.data)
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=200)

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)



@api_view(['GET'])
@permission_classes((AllowAny, ))
def activate_User(request):
    try:
        pk = request.query_params.get('pk')
        list = App_User.objects.get(user=int(pk))
        list.active = True
        list.save()
        return redirect ("http://127.0.0.1:8000/store/book/")

    except Exception as e:
        logger.info("Error")
        logger.info(str(e))
        return Response(str(e), status=200)


@api_view(['POST'])
@permission_classes((AllowAny, ))
def create_User(self, request):
    try:

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # return Response(serializer.data, status=200)
        else:
            return Response(serializer.errors, status=200)
        logger.info(serializer.data["username"])

        list = User.objects.get(username=serializer.data["username"])
        datas = request.data.copy()
        datas["user"] =list.id
        try:
            Token.objects.create(user=list)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)
        logger.info("ji")
        auth = Token.objects.get(user=list.id)
        serializer = App_UserSerializer(data=datas)
        logger.info("jay")
        if serializer.is_valid():
            serializer.save()
            datas = serializer.data.copy()
            datas["token"] = auth.key
            datas["message"] = "A verification mail will be sent to mail id to activate your account."
            logger.info(auth.key)
            logger.info(auth.key)
            smtpsender(datas,list.id)
            return Response(datas, status=200)
        else:
            return Response(serializer.errors, status=200)
        return Response(serializer.errors, status=200)


        # return Response(serializer.errors, status=200)
    except Exception as e:
        logger.info("Error")
        logger.info(str(e))
        return Response(str(e), status=200)
