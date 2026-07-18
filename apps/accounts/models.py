from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    '''Custom User model that extends the default Django User model.'''
    pass