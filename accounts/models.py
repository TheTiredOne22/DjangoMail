from django.db import models

from users.models import User


# Create your models here.

class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # avatar = models.ImageField()
