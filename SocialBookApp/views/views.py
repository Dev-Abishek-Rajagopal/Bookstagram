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

class BookVeiwSet(ModelViewSet):

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

    queryset = App_User.objects.all()
    serializer_class = App_UserSerializer


    def list_Book(self, request):
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


    def create_Book(self, request):
        try:
            serializer = App_UserSerializer(data=request.data)
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
            list = App_User.objects.get(id=pk)
            serializer = App_UserSerializer(list)
            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def delete_Book(self, request,*args, **kwargs):
        try:
            pk = self.kwargs['pk']
            item = App_User.objects.get(id=pk)
            item.delete()
            return Response(json.loads('{"response" : "Book deleted successfully."}'), status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def update_Book(self, request, *args, **kwargs):
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