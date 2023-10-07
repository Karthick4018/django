from django.db import models

# Create your models here.
class Members(models.Model):
    firstname=models.CharField(max_length=255)
    lastname=models.CharField(max_length=255)
class Person(models.Model):
    name=models.CharField(max_length=100)
    place=models.CharField(max_length=50)
class Blog(models.Model):
    title=models.CharField(max_length=100)
    content=models.CharField(max_length=3000)

