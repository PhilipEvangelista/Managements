from django.db import models
from django.utils import timezone
# Create your models here.


class History(models.Model):
    select = models.CharField(max_length=15, default='Add Debts')
    name = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    current_balance = models.FloatField(default=0)
    new_balance = models.FloatField(default=0)
    payment = models.FloatField(default=0)

    def __str__(self):
        return self.name


class Information(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)
    interest = models.FloatField(default=0)
    balance = models.FloatField(default=0)
    interest_bool = models.BooleanField(default=True)
    agreement = models.BooleanField(default=False)
    date_debts = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Security(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username


class Bitcoin(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField(default=0)
    currency = models.FloatField(default=0)
    current = models.FloatField(default=0)
    status = models.CharField(max_length=25, default='Increase')
    rank = models.IntegerField(default=1)
    url = models.CharField(max_length=500, default="https://www.coingecko.com/en/coins/plant-vs-undead-token/php")

    def __str__(self):
        return self.name

