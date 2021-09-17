from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.

class tweet(models.Model):
    tweets = models.TextField(max_length=300, default= '')
    dateTime = models.DateTimeField(default=timezone.now)
    usrName = models.ForeignKey(User,on_delete=models.CASCADE)