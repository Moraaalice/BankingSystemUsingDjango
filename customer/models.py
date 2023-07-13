from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=48)
    address = models.CharField(max_length=48)
    contact = PhoneNumberField()
    identificationNumber = models.CharField(max_length=8)

    def __str__(self):
        return self.name