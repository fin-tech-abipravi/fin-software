from django.db import models


class Costumerdetails(models.Model):
    name = models.CharField(max_length=300)
    loanammount = models.IntegerField()
    loan_date = models.CharField(max_length=300)
    loanInterst = models.IntegerField()
    ms = models.IntegerField()
    place = models.CharField(max_length=300)
    ammount_Balance = models.CharField(max_length=300)
    place_id = models.IntegerField()
    last_collected = models.CharField(max_length=300, blank=True)
    last_collected_date = models.CharField(max_length=300, blank=True)

    def __str__(self):
        return self.name


class Collectionlist(models.Model):
    date = models.CharField(max_length=300)
    costumer_id = models.IntegerField(default=0)
    costumer_name = models.CharField(max_length=300)
    ammount = models.IntegerField()

    def __str__(self):
        return self.costumer_name


class Dlammounts(models.Model):
    date = models.CharField(max_length=300)
    ammount = models.IntegerField()

    def __str__(self):
        return self.date


class Ammountinhand(models.Model):
    date = models.CharField(max_length=300)
    ammount = models.IntegerField()

    def __str__(self):
        return self.date


class Expence(models.Model):
    date = models.CharField(max_length=300)
    expenceName = models.CharField(max_length=300)
    expenceAmmount = models.CharField(max_length=300)

    def __str__(self):
        return self.expenceName


class Expencetotal(models.Model):
    date = models.CharField(max_length=300)
    ammount = models.IntegerField()

    def __str__(self):
        return self.date


class Closeup(models.Model):
    date = models.CharField(max_length=300)
    costumername = models.CharField(max_length=300)
    ammount = models.IntegerField()

    def __str__(self):
        return self.costumername


class Closedown(models.Model):
    date = models.CharField(max_length=300)
    costumername = models.CharField(max_length=300)
    ammount = models.IntegerField()

    def __str__(self):
        return self.costumername


class Otherammountin(models.Model):
    date = models.CharField(max_length=300)
    reason = models.CharField(max_length=300)
    ammount = models.IntegerField()

    def __str__(self):
        return self.reason


class Otherammountout(models.Model):
    date = models.CharField(max_length=300)
    reason = models.CharField(max_length=300)
    ammount = models.IntegerField()

    def __str__(self):
        return self.reason


class Inversment(models.Model):
    date = models.CharField(max_length=300)
    name = models.CharField(max_length=300)
    ammount = models.IntegerField()

    def __str__(self):
        return self.name

class Others(models.Model):
    date = models.CharField(max_length=300)
    reason = models.CharField(max_length=300)
    ammount = models.IntegerField()

    def __str__(self):
        return self.reason
