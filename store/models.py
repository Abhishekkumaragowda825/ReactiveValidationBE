from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=150)
    lname = models.CharField(default="Unknown",max_length=150)
    email =  models.EmailField(unique=True,max_length=20)
    gender = models.CharField(default=None, max_length=10)
    country = models.CharField(default=None, max_length=150) 
    message = models.CharField(blank=True, default=None,max_length=250)
