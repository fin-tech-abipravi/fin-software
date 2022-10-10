from django.db import models
import datetime


class UserField(models.Model):
    username = models.CharField(max_length=300)
    password = models.CharField(max_length=300)
    fullname = models.CharField(max_length=300, blank=True)
    dateofcreation = models.DateTimeField(auto_now=True)
    account_type = models.CharField(max_length=300, default="user")
    email_address = models.CharField(max_length=300)

    def __str__(self):
        return self.username


class AuthTFfield(models.Model):
    Auth = models.CharField(max_length=200)
    expires = models.DateTimeField()
    user = models.CharField(max_length=200)

    def __str__(self):
        return self.Auth

class AccessUsers(models.Model):
    user1 = models.CharField(max_length=300, blank=True)
    user2 = models.CharField(max_length=300, blank=True)
    date = models.CharField(max_length=300, default=datetime.date.today())