from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # other fields here

    def __str__(self):
        return "%s's profile" % self.user


class Question(models.Model):
    questionText = models.CharField(max_length=1000)
    image = models.ImageField()

    def __str__(self):
        return str(self.questionText)
