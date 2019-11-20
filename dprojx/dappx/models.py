# dappx/models.py
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    portfolio_site = models.URLField(blank=True)
    # profile_pic = models.ImageField(upload_to='profile_pics',blank=True)
    student_number = models.IntegerField(blank=True,default = "1" , primary_key=True)
    regno = models.CharField(max_length=30, unique=True, default = "default")
    names = models.CharField(max_length=60, default = "default")
    DOB = models.DateField(null=True)
    year_of_study = models.IntegerField(blank=True, default = "default")
    def __str__(self):
        return self.user.username
