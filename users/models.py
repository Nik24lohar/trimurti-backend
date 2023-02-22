from django.db.models.fields.related import ForeignKey
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.contrib.auth.models import AbstractUser,UserManager
from django.conf import settings
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.db.models.deletion import CASCADE
from rest_framework.authtoken.models import Token
from .managers import CustomUserManager
import uuid

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'),unique=True)
    userId =  models.AutoField(primary_key=True)
    first_name= models.CharField(max_length=200,null=True,default=None)
    last_name= models.CharField(max_length=200,null=True,default=None)
    contact_no= models.CharField(max_length=15,null=True,default=None)
    address= models.CharField(max_length=200,null=True,default=None)
    profilePic = models.URLField(default='https://cdn.pixabay.com/photo/2015/10/05/22/37/blank-profile-picture-973460_960_720.png')
    registerDate = models.DateField(auto_now=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()
