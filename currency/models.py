from django.db import models
from forex_python.converter import CurrencyRates

# Create your models here.
class CurrencyExchangeField(models.DecimalField):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.c = CurrencyRates()


class Currency(models.Model):
    code = models.CharField(max_length=10)
    exchange_rate = CurrencyExchangeField(max_digits=10, decimal_places=2)
    name = models.CharField(max_length=48,default="")

    def __str__(self):
        return self.code


