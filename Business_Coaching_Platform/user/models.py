from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    is_coach = models.BooleanField(default = False)
    is_coachee = models.BooleanField(default = False)
    email = models.EmailField(unique = True)
    age = models.IntegerField(null = True)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'All_User'


class Coach(CustomUser): 
    description = models.TextField()
    
    class Meta:    
        verbose_name = 'Coach'


class Coachee(CustomUser): 
    
    class Meta:
        verbose_name = 'Coachee'