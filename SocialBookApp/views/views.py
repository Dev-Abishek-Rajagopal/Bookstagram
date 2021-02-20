'''
Created on 20-JAN-2021

@author: Abishek Rajagopal
'''


from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from SocialBookApp.models.bookmodels import (Book,TextBook,BookComments,OwnBook,BookWishlist)
from SocialBookApp.models.usermodels import (App_User,friendlist,profileTXTPost,TXTPostComments,profileComment)
from django.contrib.auth.models import User
from SocialBookApp.serializers.serializers import (BookSerializer,BookSerializerI,App_UserSerializer,UserSerializer,friendlistSerializer,profileTXTPostSerializer,App_UserSerializerI,profileTXTPostSerializerI,TXTPostCommentsSerializer,TXTPostCommentsSerializerI,profileCommentSerializer,TextBookSerializer,TextBookSerializerI,BookCommentsSerializer,OwnBookSerializer,OwnBookSerializerI,WishlistSerializer,profileCommentSerializerI,BookCommentsSerializerI,WishlistSerializerI  )
from rest_framework.response import Response
import logging
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser
import json
from rest_framework.authtoken.models import (Token)
from SocialBookApp.views.process import (smtpsender)
from django.shortcuts import redirect
from rest_framework.permissions import AllowAny
from django.db.models import Q
from django.forms.models import model_to_dict
from itertools import chain
from django.core import serializers

logger = logging.getLogger("book.request")

class BookVeiwSet(ModelViewSet):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializer


    def list_Book(self, request):
        try:
            book_list = Book.objects.all()
            serializer = BookSerializerI(book_list, many=True)
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
            serializer = BookSerializerI(data=request.data)
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
            serializer = BookSerializerI(list)
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
                pk = self.kwargs['pk']
                list = Book.objects.get(id=pk)
                serializer = BookSerializerI(list)

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
def create_User(request):
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

class friendlistVeiwSet(ModelViewSet):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = friendlist.objects.all()
    serializer_class = friendlistSerializer

    def create_relationship(self, request):
        try:
            serializer = friendlistSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def update_relationship(self, request, *args, **kwargs):
        try:
            serializer = friendlistSerializer(data=request.data)
            pk = self.kwargs['pk']
            item = friendlist.objects.get(id=pk)
            if serializer.is_valid():
                datas = serializer.data.copy()
                if datas['relationship'] == 'friends':
                    list = App_User.objects.get(id=datas["user"])
                    list.friends = list.friends + 1
                    list.save()
                    list = App_User.objects.get(id=datas["friend"])
                    list.friends = list.friends + 1
                    list.save()
                serializer.update(item, serializer.data)
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def get_friendlist(self, request,*args, **kwargs):
        try:
            pk = self.kwargs['pk']
            datas =[]
            dbi = friendlist.objects.filter(Q(user_id=int(pk)) & Q(relationship="friends") | Q(friend_id=int(pk)) & Q(relationship="friends") )
            logger.info("hi")
            logger.info(dbi)
            arr = []
            for i in dbi:
                if i.user_id == int(pk):
                    logger.info("hi")
                    logger.info(i.friend)
                    list = App_User.objects.get(id=i.friend_id)
                    logger.info(list)
                    serializer = App_UserSerializerI(list)
                    arr.append(serializer.data)
                if i.friend_id == int(pk):
                    logger.info("hi")
                    logger.info(i.user)
                    list = App_User.objects.get(id=i.user_id)
                    serializer = App_UserSerializerI(list)
                    arr.append(serializer.data)
            # serializer = friendlistSerializer(dbi, many=True)
            logger.info(dbi)
            logger.info("dbi")
            logger.info(arr)
            serializer = App_UserSerializer("arr", many=True)
            return Response(arr, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def get_profile(self, request,*args, **kwargs):
        try:
            pk = request.query_params.get('pk')
            list = App_User.objects.get(id=pk)
            serializer = App_UserSerializerI(list)
            # auth = Token.objects.get(user=pk)
            datas = serializer.data.copy()
            # datas["token"] = auth.key
            # logger.info(auth.key)
            return Response(datas, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def get_acceptfriendlist(self, request,*args, **kwargs):
        try:
            pk = self.kwargs['pk']
            datas =[]
            dbi = friendlist.objects.filter(Q(friend_id=int(pk)) & Q(relationship="addfriend") )
            logger.info("hi")
            logger.info(dbi)
            serializer = friendlistSerializer(dbi, many=True)

            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def get_allUsers(self, request,*args, **kwargs):
        try:
            App_User_list = App_User.objects.all()
            serializer = App_UserSerializerI(App_User_list, many=True)
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

    def get_allUserstype(self, request,*args, **kwargs):
        try:
            App_User_list = App_User.objects.all()
            pk = request.query_params.get('type')

            dbi = App_User.objects.filter(Q(usertype=(pk)))

            serializer = App_UserSerializerI(dbi, many=True)
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

    def get_notfriendlist(self, request,*args, **kwargs):
        try:
            pk = self.kwargs['pk']
            datas = []
            datas =[]
            dbi = friendlist.objects.filter(Q(user_id=int(pk)) & Q(relationship="addfriend")  )
            logger.info("hi")
            logger.info(dbi)
            serializer = friendlistSerializer(dbi, many=True)

            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)


    def Unfriend(self, request,*args, **kwargs):
        try:
            pk = self.kwargs['pk']
            item = friendlist.objects.get(id=pk)
            item.delete()
            return Response(json.loads('{"response" : "Unfriend or Ignored successfully."}'), status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)


    def list_friendlist(self, request):
        try:
            friendlist_list = friendlist.objects.all()
            serializer = friendlistSerializer(friendlist_list, many=True)
            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

class profileTXTPostVeiwSet(ModelViewSet):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = profileTXTPost.objects.all()
    serializer_class = profileTXTPostSerializer


    def create_profileTXTPost(self, request):
        try:
            serializer = profileTXTPostSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def list_profile_post(self, request):
        try:
            pk = request.query_params.get('pk')
            dbi = profileTXTPost.objects.filter(Q(user_id=int(pk)) )
            logger.info("hi")
            logger.info(dbi)
            serializer = profileTXTPostSerializer(dbi, many=True)
            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def list_home_post(self, request):

        try:
            pk = request.query_params.get('pk')
            datas = []
            dbi = friendlist.objects.filter(
                Q(user_id=int(pk)) & Q(relationship="friends") | Q(friend_id=int(pk)) & Q(relationship="friends"))
            logger.info("hi")
            logger.info(dbi)
            arr = []
            for i in dbi:
                if i.user_id == int(pk):
                    logger.info("hi")
                    logger.info(i.friend)
                    list = App_User.objects.get(id=i.friend_id)
                    logger.info(list)
                    serializer = App_UserSerializerI(list)
                    arr.append(serializer.data)
                if i.friend_id == int(pk):
                    logger.info("hi")
                    logger.info(i.user)
                    list = App_User.objects.get(id=i.user_id)
                    serializer = App_UserSerializerI(list)
                    arr.append(serializer.data)
            # serializer = friendlistSerializer(dbi, many=True)
            logger.info(dbi)
            logger.info("dbi")
            logger.info(arr)
            postarr = []
            dbi = profileTXTPost.objects.filter(Q(user_id=int(pk)))
            logger.info("hi")
            logger.info(dbi)
            logger.info("hii")
            serializer = profileTXTPostSerializer(dbi, many=True)
            for i in serializer.data:
                postarr.append(i)
            for i in arr:
                dbi = profileTXTPost.objects.filter(Q(user_id=int(i["id"])))
                logger.info("hii")
                logger.info(dbi)
                serializer1 = profileTXTPostSerializer(dbi, many=True)
                for j in serializer1.data:
                    postarr.append(j)

            logger.info(postarr)
            postarr = sorted(postarr, key=lambda k: k['publist'])
            return Response(postarr, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)


    def delete_Post(self, request,*args, **kwargs):
        try:
            pk = self.kwargs['pk']
            item = profileTXTPost.objects.get(id=pk)
            item.delete()
            return Response(json.loads('{"response" : "Post deleted successfully."}'), status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def update_Post(self, request, *args, **kwargs):
        try:
            serializer = profileTXTPostSerializerI(data=request.data)
            pk = self.kwargs['pk']
            item = profileTXTPost.objects.get(id=pk)
            logger.info(item)
            if serializer.is_valid():
                logger.info("hi")
                serializer.update(item, serializer.data)
            else:
                return Response(serializer.errors, status=200)

            list = profileTXTPost.objects.get(id=pk)
            serializer = profileTXTPostSerializer(list)
            return Response(serializer.data, status=200)

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

class TXTPostCommentsVeiwSet(ModelViewSet):

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = TXTPostComments.objects.all()
    serializer_class = TXTPostCommentsSerializer


    def list_TXTPostComments(self, request):
        try:
            book_list = TXTPostComments.objects.all()
            serializer = TXTPostCommentsSerializer(book_list, many=True)

            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def list_Spec_TXTPostComments(self, request):
        try:
            book_list = TXTPostComments.objects.all()
            pk = request.query_params.get('pk')
            dbi = TXTPostComments.objects.filter(
                Q(post_id=int(pk)))
            serializer1 = TXTPostCommentsSerializer(dbi, many=True)
            return Response(serializer1.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def create_TXTPostComments(self, request):
        try:
            serializer = TXTPostCommentsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                datas = serializer.data.copy()
                list = profileTXTPost.objects.get(id=datas["post"])
                list.comments = list.comments + 1
                list.save()
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def get_TXTPostComments(self, request,*args, **kwargs):
        try:
            pk = self.kwargs['pk']
            list = TXTPostComments.objects.get(id=pk)
            serializer = TXTPostCommentsSerializer(list)
            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def delete_TXTPostComments(self, request,*args, **kwargs):
        try:
            pk = self.kwargs['pk']
            item = TXTPostComments.objects.get(id=pk)
            item.delete()
            return Response(json.loads('{"response" : "Comment deleted successfully."}'), status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def update_TXTPostComments(self, request, *args, **kwargs):
        try:
            serializer = TXTPostCommentsSerializerI(data=request.data)
            pk = self.kwargs['pk']
            logger.info("hi")
            item = TXTPostComments.objects.get(id=pk)
            if serializer.is_valid():
                serializer.update(item, serializer.data)
                pk = self.kwargs['pk']
                list = TXTPostComments.objects.get(id=pk)
                serializer = TXTPostCommentsSerializer(list)
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=200)

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)



class profileCommentVeiwSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = profileComment.objects.all()
    serializer_class = profileCommentSerializer

    def list_profileComment(self, request):
        try:
            book_list = profileComment.objects.all()
            serializer = profileCommentSerializer(book_list, many=True)

            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def create_profileComment(self, request):
        try:
            serializer = profileCommentSerializer(data=request.data)
            logger.info(serializer.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def get_profileComment(self, request, *args, **kwargs):
        try:
            pk = self.kwargs['pk']
            list = profileComment.objects.get(id=pk)
            serializer = profileCommentSerializer(list)
            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def get_profileCommentbyuser(self, request, *args, **kwargs):
        try:

            pk = request.query_params.get('pk')
            dbi = profileComment.objects.filter(Q(user_id=int(pk)) )
            logger.info("hi")
            logger.info(dbi)
            serializer = profileCommentSerializer(dbi, many=True)
            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def delete_profileComment(self, request, *args, **kwargs):
        try:
            pk = self.kwargs['pk']
            item = profileComment.objects.get(id=pk)
            item.delete()
            return Response(json.loads('{"response" : "Comment deleted successfully."}'), status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def update_profileComment(self, request, *args, **kwargs):
        try:
            serializer = profileCommentSerializerI(data=request.data)
            pk = self.kwargs['pk']
            item = profileComment.objects.get(id=pk)
            logger.info('hi')
            if serializer.is_valid():
                serializer.update(item, serializer.data)
                pk = self.kwargs['pk']
                list = profileComment.objects.get(id=pk)
                serializer = profileCommentSerializer(list)
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=200)

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)


class TextBookVeiwSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = TextBook.objects.all()
    serializer_class = TextBookSerializer

    def list_TextBook(self, request):
        try:
            book_list = TextBook.objects.all()
            serializer = TextBookSerializer(book_list, many=True)

            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def create_TextBook(self, request):
        try:
            serializer = TextBookSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def get_TextBook(self, request, *args, **kwargs):
        try:
            pk = self.kwargs['pk']
            list = TextBook.objects.get(id=pk)
            serializer = TextBookSerializer(list)
            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def delete_TextBook(self, request, *args, **kwargs):
        try:
            pk = self.kwargs['pk']
            item = TextBook.objects.get(id=pk)
            item.delete()
            return Response(json.loads('{"response" : "TextBook deleted successfully."}'), status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def update_TextBook(self, request, *args, **kwargs):
        try:
            serializer = TextBookSerializerI(data=request.data)
            pk = self.kwargs['pk']
            item = TextBook.objects.get(id=pk)
            if serializer.is_valid():
                serializer.update(item, serializer.data)
                pk = self.kwargs['pk']
                list = TextBook.objects.get(id=pk)
                serializer = TextBookSerializer(list)
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=200)

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)


class BookCommentsVeiwSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = BookComments.objects.all()
    serializer_class = BookCommentsSerializer

    def list_BookComments(self, request):
        try:
            book_list = BookComments.objects.all()
            serializer = BookCommentsSerializer(book_list, many=True)

            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def create_BookComments(self, request):
        try:
            serializer = BookCommentsSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def get_BookComments(self, request, *args, **kwargs):
        try:
            pk = self.kwargs['pk']
            list = BookComments.objects.get(id=pk)
            serializer = BookCommentsSerializer(list)
            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def get_BookCommentsyou(self, request, *args, **kwargs):
        try:

            pk = request.query_params.get('pk')
            dbi = BookComments.objects.filter(Q(user_id=int(pk)) )
            logger.info("hi")
            logger.info(dbi)
            serializer = BookCommentsSerializer(dbi, many=True)
            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def get_BookCommentsbybook(self, request, *args, **kwargs):
        try:

            pk = request.query_params.get('pk')
            dbi = BookComments.objects.filter(Q(Book_id=int(pk)) )
            logger.info("hi")
            logger.info(dbi)
            serializer = BookCommentsSerializer(dbi, many=True)
            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def delete_BookComments(self, request, *args, **kwargs):
        try:
            pk = self.kwargs['pk']
            item = BookComments.objects.get(id=pk)
            item.delete()
            return Response(json.loads('{"response" : "Comment deleted successfully."}'), status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def update_BookComments(self, request, *args, **kwargs):
        try:
            serializer = BookCommentsSerializerI(data=request.data)
            pk = self.kwargs['pk']
            item = BookComments.objects.get(id=pk)
            if serializer.is_valid():
                serializer.update(item, serializer.data)
                pk = self.kwargs['pk']
                list = BookComments.objects.get(id=pk)
                serializer = BookCommentsSerializer(list)
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=200)

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)


class OwnBookVeiwSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = OwnBook.objects.all()
    serializer_class = OwnBookSerializer

    def list_OwnBook(self, request):
        try:
            book_list = OwnBook.objects.all()
            serializer = OwnBookSerializer(book_list, many=True)

            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def create_OwnBook(self, request):
        try:
            serializer = OwnBookSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def get_OwnBook(self, request, *args, **kwargs):
        try:
            pk = self.kwargs['pk']
            list = OwnBook.objects.get(id=pk)
            serializer = OwnBookSerializer(list)
            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def get_OwnBookyou(self, request, *args, **kwargs):
        try:

            pk = request.query_params.get('pk')
            dbi = OwnBook.objects.filter(Q(user_id=int(pk)) )
            logger.info("hi")
            logger.info(dbi)
            serializer = OwnBookSerializer(dbi, many=True)
            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def get_OwnBookbybook(self, request, *args, **kwargs):
        try:

            pk = request.query_params.get('pk')
            dbi = OwnBook.objects.filter(Q(Book_id=int(pk)) )
            logger.info("hi")
            logger.info(dbi)
            serializer = OwnBookSerializer(dbi, many=True)
            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def get_OwnBookbybookUser(self, request, *args, **kwargs):
        try:

            pk = request.query_params.get('pk')
            user = request.query_params.get('user')
            dbi = OwnBook.objects.filter(Q(Book_id=int(pk)) & Q(user_id=int(user)))
            logger.info("hi")
            logger.info(dbi)
            serializer = OwnBookSerializer(dbi, many=True)
            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def delete_OwnBook(self, request, *args, **kwargs):
        try:
            pk = self.kwargs['pk']
            item = OwnBook.objects.get(id=pk)
            item.delete()
            return Response(json.loads('{"response" : "Book owned record deleted successfully."}'), status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def update_OwnBook(self, request, *args, **kwargs):
        try:
            serializer = OwnBookSerializerI(data=request.data)
            pk = self.kwargs['pk']
            item = OwnBook.objects.get(id=pk)
            if serializer.is_valid():
                serializer.update(item, serializer.data)
                pk = self.kwargs['pk']
                list = OwnBook.objects.get(id=pk)
                serializer = OwnBookSerializer(list)
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=200)

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)


class WishlistVeiwSet(ModelViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = BookWishlist.objects.all()
    serializer_class = WishlistSerializer

    def list_Wishlist(self, request):
        try:
            book_list = BookWishlist.objects.all()
            serializer = WishlistSerializer(book_list, many=True)

            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def create_Wishlist(self, request):
        try:
            serializer = WishlistSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def get_Wishlist(self, request, *args, **kwargs):
        try:
            pk = self.kwargs['pk']
            list = BookWishlist.objects.get(id=pk)
            serializer = WishlistSerializer(list)
            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def get_Wishlistyou(self, request, *args, **kwargs):
        try:

            pk = request.query_params.get('pk')
            dbi = BookWishlist.objects.filter(Q(user_id=int(pk)) )
            logger.info("hi")
            logger.info(dbi)
            serializer = WishlistSerializer(dbi, many=True)
            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def get_Wishlistbybook(self, request, *args, **kwargs):
        try:

            pk = request.query_params.get('pk')
            dbi = BookWishlist.objects.filter(Q(Book_id=int(pk)) )
            logger.info("hi")
            logger.info(dbi)
            serializer = WishlistSerializer(dbi, many=True)
            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def get_WishlistbybookUser(self, request, *args, **kwargs):
        try:

            pk = request.query_params.get('pk')
            user = request.query_params.get('user')
            dbi = BookWishlist.objects.filter(Q(Book_id=int(pk)) & Q(user_id=int(user)))
            logger.info("hi")
            logger.info(dbi)
            serializer = WishlistSerializer(dbi, many=True)
            return Response(serializer.data, status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def delete_Wishlist(self, request, *args, **kwargs):
        try:
            pk = self.kwargs['pk']
            item = BookWishlist.objects.get(id=pk)
            item.delete()
            return Response(json.loads('{"response" : "Book removed from Wishlist."}'), status=200)
        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)

    def update_Wishlist(self, request, *args, **kwargs):
        try:
            serializer = WishlistSerializerI(data=request.data)
            pk = self.kwargs['pk']
            item = BookWishlist.objects.get(id=pk)
            if serializer.is_valid():
                serializer.update(item, serializer.data)
                pk = self.kwargs['pk']
                list = BookWishlist.objects.get(id=pk)
                serializer = WishlistSerializer(list)
                return Response(serializer.data, status=200)
            return Response(serializer.errors, status=200)

        except Exception as e:
            logger.info("Error")
            logger.info(str(e))
            return Response(str(e), status=200)



















