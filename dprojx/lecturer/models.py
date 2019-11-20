# dappx/models.py
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class LecturerInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    name=models.CharField(max_length=30, null=True)
    college = models.CharField(max_length=30)
    department = models.CharField(max_length=30, null=True)
    lecturer_id = models.IntegerField()
    def __str__(self):
        return self.user.username