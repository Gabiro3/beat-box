from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, name=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, username, password, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=True)
    name = models.CharField(max_length=150, unique=True, null=True)
    avatar = models.ImageField(null=False, default='avatar.svg')

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email
# Music model
class Music(models.Model):
    title = models.CharField(max_length=120, null=True)
    music_type = models.CharField(max_length=100, null=True)
    creator = models.CharField(max_length=120, null=True)
    
    # New fields
    cover = models.ImageField(null=True)
    downloadable = models.BooleanField(default=True)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.title
    

class Artist(models.Model):
    name = models.CharField(max_length=120, null=True)
    music =  models.ManyToManyField(Music, blank=True)
    genre = models.CharField(max_length=100, null=True)
    cover = models.ImageField(null=True)
    created_by = models.CharField(max_length=120, null=True)
    uploaded = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ['-uploaded']

class Sample(models.Model):
    title = models.CharField(max_length=100, null=True)
    album = models.CharField(max_length=120, null=True)
    music_type = models.CharField(max_length=100, null=True)
    creator = models.CharField(max_length=100, null=True)
    sample = models.FileField(upload_to='samples', null=True)
    duration = models.FloatField(null=True)

class Melody(models.Model):
    genre = models.CharField(max_length=100, null=True)
    content = models.FileField(upload_to='melodies', null=True)
