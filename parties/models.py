from django.db import models

# Create your models here.


class Parties(models.Model):
    name = models.CharField(max_length=300)
    place = models.CharField(max_length=300)
    email_id = models.CharField(
        max_length=300, default='none', null=True, blank=True)
    place_id = models.IntegerField()
    contact = models.IntegerField(default=0000000000, null=True)

    def __str__(self):
        return self.name


class Partyloans(models.Model):
    party_id = models.IntegerField(default=0)
    loan_id = models.IntegerField(default=0)

    def __int__(self):
        return self.loan_id
