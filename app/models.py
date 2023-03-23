from django.db import models

# Create your models here.

class User(models.Model):
    contact=models.IntegerField()
    email=models.EmailField(max_length=254)
    password=models.CharField(max_length=50)

class Student(models.Model):
    name=models.CharField(max_length=50)
    contact=models.IntegerField()
    section=models.CharField(max_length=50)
    school=models.CharField(max_length=50)