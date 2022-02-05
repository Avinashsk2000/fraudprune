from django.db import models
from django.db.models.fields import EmailField
import uuid

# Create your models here.


class customer(models.Model):
    name = models.CharField(max_length=20)
    Email = models.EmailField(primary_key=True)
    phone_number = models.CharField(max_length=10)
    account_number = models.CharField(max_length=15)
    PIN = models.CharField(max_length=255)
    balance = models.IntegerField()


class register_acc(models.Model):
    Email = models.EmailField(primary_key=True)
    account_number = models.CharField(max_length=15)
    New_PIN = models.CharField(max_length=255)


class transaction(models.Model):
    Email = models.EmailField(primary_key=True)
    amount = models.IntegerField()
    unique_code_s = models.UUIDField(default=uuid.uuid4)
