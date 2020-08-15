from django.shortcuts import render
from myapp.serializers import PersonSerializers
from rest_framework import viewsets
from myapp.models import Person


# Create your views here.
class Personviewset(viewsets.ModelViewSet):
    serializer_class=PersonSerializers
    queryset=Person.objects.all()