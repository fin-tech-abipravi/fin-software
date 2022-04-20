from django.db import models

# Create your models here.


class Parties(Models.model):
    name = models.CharField(max_length=300)
    place = models.CharField(max_length=300)
    ammount_Balance = models.CharField(max_length=300)
    place_id = models.IntegerField()
    contact = models.IntegerField()

    def __str__(self):
        return self.name
