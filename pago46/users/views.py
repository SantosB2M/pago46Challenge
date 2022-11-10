from django.shortcuts import render
from .serializer import UserSerializer, UserIOUSerializer
from rest_framework import viewsets
from users.models import User
# Create your views here.

class UserIOUViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('last_name')
    serializer_class = UserIOUSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('last_name')
    serializer_class = UserSerializer