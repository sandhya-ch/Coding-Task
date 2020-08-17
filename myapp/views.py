from django.shortcuts import render
from myapp.serializers import PersonSerializers
from rest_framework import viewsets
from myapp.models import Person
import pandas as pd
from django.http import HttpResponse
from rest_framework import permissions
from .forms import UploadFileForm


# Create your views here.
class Personviewset(viewsets.ModelViewSet):
    serializer_class=PersonSerializers
    queryset=Person.objects.all()
    permission_classes = [permissions.AllowAny]

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file=request.FILES['file']
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
            return HttpResponse("<h1>Successfully data inserted</h1>")
    else:
        form = UploadFileForm()
    return render(request, 'index.html', {'form': form})