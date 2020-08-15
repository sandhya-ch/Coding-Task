from django.db import models
from model_utils.models import TimeStampedModel

# Create your models here.
class Person(TimeStampedModel):
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    designation=models.CharField(max_length=50)

    def __str__(self):
        return self.name




