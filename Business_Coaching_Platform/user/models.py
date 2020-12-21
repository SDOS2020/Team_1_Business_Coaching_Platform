from django.db import models
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from phonenumber_field.modelfields import PhoneNumberField


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email = self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using = self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password = password
        )
        user.is_admin = True
        user.save(using = self._db)
        return user


class CustomUser(AbstractBaseUser):
    is_coach = models.BooleanField(default = False)
    is_coachee = models.BooleanField(default = False)
    email = models.EmailField(verbose_name = 'email address', max_length = 255, unique = True)
    age = models.IntegerField(null = True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = "Users"

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Coach(models.Model):
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE) 
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    description = models.TextField(max_length = 1000, null = True, blank = True)
    profile_photo = models.ImageField(null = True, blank = True, upload_to = 'profile_photos')
    linkedin = models.URLField(max_length = 100, blank = True, null = True)
    location = models.CharField(max_length = 100, null = True, blank = True)
    coaching_hours = models.IntegerField(blank=True, null=True)
    area_of_expertise = models.TextField(max_length = 1000)
    class Meta:    
        verbose_name = 'Coach'
        verbose_name_plural = "Coaches"
        ordering = ("last_name", "first_name")
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Coachee(models.Model): 
    user = models.OneToOneField(CustomUser, on_delete = models.CASCADE)
    first_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    profile_photo = models.ImageField(null = True, blank = True, upload_to = 'profile_photos')
    linkedin = models.URLField(max_length = 100, blank = True, null = True)
    location = models.CharField(max_length = 100, blank = True, null = True)
    resume = models.FileField(upload_to='resume_uploads', blank = True, null = True)
    purpose = models.TextField(max_length = 1000, blank = True, null = True)
    contact = PhoneNumberField(blank = True, null = True)
    class Meta:
        verbose_name = 'Coachee'
        verbose_name_plural = "Coachees"
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Connection(models.Model):
    coach = models.ForeignKey(Coach, on_delete = models.CASCADE)
    coachee = models.ForeignKey(Coachee, on_delete = models.CASCADE)
    accepted = models.BooleanField(default = False)

    def __str__(self):
        return f"{self.coach} coaches {self.coachee} : {self.accepted}"
    
    class Meta:
        verbose_name = 'Connection'
        verbose_name_plural = "Connections"
        unique_together = ['coach', 'coachee']