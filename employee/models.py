from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

position_choices = (
    ("branch manager","Branch Manager"),
    ("cashier","Cashier"),
    ("supervisor","Supervisor"),
    ("technical engineer","Technical Engineer"),
    ("support staff","Support Staff"),
)


# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=48)
    contact = PhoneNumberField()
    position = models.CharField(max_length=48,choices=position_choices)
    identificationNuber = models.CharField(max_length=48)

