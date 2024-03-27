from django.db import models

# Create your models here.

class Student(models.Model):
    roll = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    address = models.CharField(max_length=50)


