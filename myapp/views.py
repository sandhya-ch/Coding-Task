from django.shortcuts import render
from myapp.serializers import PersonSerializers
from rest_framework import viewsets
from myapp.models import Person
import pandas as pd
from rest_framework.response import Response
from rest_framework import permissions

# Create your views here.
class Personviewset(viewsets.ModelViewSet):
    serializer_class=PersonSerializers
    queryset=Person.objects.all()
    permission_classes = [permissions.AllowAny]

    def create(self, request):
        data = request.data
        name = data.get('name',None)
        age = data.get('age',None)
        designation = data.get('designation',None)
        file=request.FILES.get('file',None)
        if file:
            csv_data=pd.read_csv(file)
            personObjs = [
                Person(
                    name = row['Name'],
                    age = row['Age'],
                    designation = row['Designation']
                )
                for index,row in csv_data.iterrows()
            ]
            Person.objects.bulk_create(personObjs)
        else:
            Person.objects.create(name=name,age=age,designation=designation)
        return Response({"message":'Successfully data inserted'})