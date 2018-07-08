from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.generics import (ListAPIView, RetrieveAPIView ,UpdateAPIView, DestroyAPIView, CreateAPIView, ListCreateAPIView )
from .models import album
from .serializer import AlbumSerializer, AlbumSerializerlist,  UserCreateSerializer ,UserLoginSerializer
from rest_framework.permissions import  (AllowAny,IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly)
# Create your views here.

user=get_user_model()
class AblumListView(CreateAPIView): # it displays the whole list
    queryset = album.objects.all()
    serializer_class = AlbumSerializerlist


class AblumdetailView(RetrieveAPIView): # it displays one item from the list according lookup field by default it's the pk
    queryset = album.objects.all()
    serializer_class = AlbumSerializer
    lookup_field="title"
    #lookup_url_kwarg="abc"

class AblumUpdateView(UpdateAPIView): # it displays the whole list
    queryset = album.objects.all()
    serializer_class = AlbumSerializer
    lookup_field="title"


class AblumDeleteView(DestroyAPIView): # it displays the whole list
    queryset = album.objects.all()
    serializer_class = AlbumSerializer
    lookup_field="title"


class UsersCreate(CreateAPIView): # icreates new users
    queryset = user.objects.all()
    serializer_class =  UserCreateSerializer

# class UserLoginSerializer(APIView): #this is the base APIView
#     permission_classes=[AllowAny] #'cause we want anyone to be able to login
#     queryset = user.objects.all()
#     serializer_class =  UserCreateSerializer




# class AblumCreateView(CreateAPIView): # it displays the whole list
#     queryset = album.objects.all()
#     serializer_class = AlbumSerializer
#     #lookup_field="title"
