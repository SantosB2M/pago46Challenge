from django.shortcuts import render
from .serializer import IOUModelSerializer
from rest_framework import viewsets
from finance.models import IOU
# Create your views here.

class IOUViewSet(viewsets.ModelViewSet):
    queryset = IOU.objects.all().order_by('value')
    serializer_class = IOUModelSerializer
