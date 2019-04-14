from django.db import models
from django.contrib.auth.models import User
from django.db.models import Count


# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    rating = models.IntegerField()
    avatar = models.ImageField(upload_to='', blank=True)

    def __str__(self):
        return self.user.username


class Tag(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name
