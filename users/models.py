from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(db_index=True, null=True, unique=True)
    date_added = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    role = models.CharField(max_length=50, blank=True, null=True)
    REQUIRED_FIELDS=['username']
    USERNAME_FIELD = 'email'

