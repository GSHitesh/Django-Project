from distutils.command.upload import upload
import email
from unittest.util import _MAX_LENGTH
from django.db import models
import email
from unittest.util import _MAX_LENGTH



# def __str__(self)-> str:
#     return self.skillname

# Create your models here.

class Register(models.Model):
    firstname = models.CharField(max_length=100)
    middlename = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    gender = models.CharField(max_length=10)
    profile_pic = models.ImageField(upload_to="profile_pic")

    def __str__(self)-> str:
        return self.firstname

