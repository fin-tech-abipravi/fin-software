from django.db import models
from datetime import date


class Costumers(models.Model):
    costumer_id = models.IntegerField()
    costumer_name = models.CharField(max_length=300)
    place = models.CharField(max_length=300)
    loandate = models.CharField(max_length=300)
    loanammount = models.IntegerField()
    loanintrest = models.IntegerField()
    loanclose = models.DateField(auto_now_add=True)
    ms = models.IntegerField()

    def __str__(self):
        return self.costumer_name


class Loandetails(models.Model):
    date = models.CharField(max_length=300)
    costumer_id = models.IntegerField()
    costumer_name = models.CharField(max_length=300)
    ammount = models.IntegerField()

    def __str__(self):
        return self.costumer_name
