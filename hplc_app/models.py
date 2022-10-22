from django.db import models
from django.contrib.auth.models import User
import uuid



class graph_input(models.Model):
    #user = models.OneToOneField(User, null = True, on_delete=models.CASCADE)
    x_min = models.IntegerField(null=True)
    x_max = models.IntegerField(null=True)
    y_min = models.IntegerField(null=True)
    y_max = models.IntegerField(null=True)

    #graph_picture = models.ImageField(null=True, blank=True)


# Create your models here.
class Image_Axes(models.Model):
    title = models.CharField(primary_key=True, max_length=100, help_text='Enter an image title')
    image = models.FileField(null=True, blank=True, upload_to='images/')
    x_min = models.IntegerField(null=True)
    x_max = models.IntegerField(null=True)
    y_min = models.IntegerField(null=True)
    y_max = models.IntegerField(null=True)

    #def __str__(self):
    #    return self.title

class ConvertImage(models.Model):
    filename = models.CharField(primary_key=True, max_length=100, help_text='Enter csv filename')