from django.db import models

different_transactions=(
        ("withdrawal","Withdrawal"),
        ("deposit","Deposit"),
    )

# Create your models here.
class Transaction(models.Model):
    transactionIdentificationNumber = models.CharField(max_length=20)
    TransactionType = models.CharField(max_length=10,choices=different_transactions)
    amount = models.DecimalField(decimal_places=2,max_digits=10)
    date = models.DateTimeField()

    def __str__(self):
        return self.transactionIdentificationNumber

