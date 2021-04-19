from django.shortcuts import render
from RestAPI.serializers import *
from rest_framework import generics
from RestAPI.models import *
# GET , POST
class makananList(generics.ListCreateAPIView):
    queryset = makanan.objects.all()
    serializer_class = makananSerializers

#GET , PUT , PATCH , DELETE
class makananDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = makanan.objects.all()
    serializer_class = makananSerializers

    
