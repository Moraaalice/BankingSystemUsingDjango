from django.db import models
from phonenumber_field.modelfields import PhoneNumberField




# Create your models here.
class BankBranch(models.Model):
    branchName = models.CharField(max_length=48)
    branchAddress = models.CharField(max_length=48)
    contactDetails = PhoneNumberField()

    def __str__(self):
        return self.branchName
    
    

    
