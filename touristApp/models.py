import uuid
import os

from django.db import models


def get_image_path(instance, filename):
    return os.path.join('photos', str(instance.id), filename)


# Create your models here.
# Layout models
class TravelCountry(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    price = models.IntegerField()
    cardDescription = models.TextField(null=True, blank=True)
    duration = models.IntegerField()
    personNum = models.IntegerField()
    #advTour = models.ManyToOneRel('TravelCountryInclude')
   # disTour = models.ManyToOneRel('TravelCountryInclude')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title  # in Admin it shows the name of the data


# Country tour fragments
class TravelCountryDescription(models.Model):
    id = models.ForeignKey(TravelCountry, on_delete=models.CASCADE, primary_key=True)
    description = models.TextField()


class TravelCountryProgram(models.Model):
    id = models.ForeignKey(TravelCountry, on_delete=models.CASCADE, primary_key=True)


class TravelCountryInclude(models.Model):
    id = models.ForeignKey(TravelCountry, on_delete=models.CASCADE, primary_key=True)

    inTour = models.TextField()  # make  it one to many?
    outTour = models.TextField()  # make it one to many?


#  Medical Tours
class TravelMed(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    country = models.CharField(max_length=100)
    photo = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    price = models.IntegerField()
    description = models.TextField(null=True, blank=True)


# Hot tours

class TravelHot(models.Model):
    country = models.CharField(max_length=100)
    photo = models.ImageField(upload_to=get_image_path, blank=True, null=True)
    price = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    days = models.IntegerField()
    personNum = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
