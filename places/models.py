from django.db import models

# Create your models here.


class Places(models.Model):
    place_id = models.IntegerField()
    place = models.CharField(max_length=300)

    def __str__(self):
        return self.place
