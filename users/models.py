from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username= None
    email = models.EmailField(db_index=True, null=True, unique=True)
    date_added = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    REQUIRED_FIELDS=[]
    USERNAME_FIELD = 'email'

