from django.db import models

# Create your models here.
class Users(models.Model):
  firstname = models.CharField(max_length=255)
  lastname = models.CharField(max_length=255)
  email = models.EmailField(max_length=50)
  phone = models.CharField(max_length=255)

