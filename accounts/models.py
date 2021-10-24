from django.db import models


class UserField(models.Model):
    username = models.CharField(max_length=300)
    password = models.CharField(max_length=300)
    email_address = models.CharField(max_length=300)

    def __str__(self):
        return self.username


class AuthTFfield(models.Model):
    Auth = models.CharField(max_length=200)
    expires = models.DateTimeField()
    user = models.CharField(max_length=200)

    def __str__(self):
        return self.Auth
