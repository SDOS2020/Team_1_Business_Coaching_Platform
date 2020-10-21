from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    is_coach = models.BooleanField(default = False)
    is_coachee = models.BooleanField(default = False)
    email = models.EmailField(unique = True)
    age = models.IntegerField(null=True)

    def __str__(self):
        return self.username


class Coach(models.Model): 
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE, primary_key = True)
    description = models.TextField()


class Coachee(models.Model): 
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE, primary_key=True)
    