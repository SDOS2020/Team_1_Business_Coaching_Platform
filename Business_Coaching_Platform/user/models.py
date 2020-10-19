from django.db import models

class Coach(models.Model): 
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    description = models.TextField()

class Coachee(models.Model): 
    firstName = models.CharField(max_length=100)
    lastName = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    