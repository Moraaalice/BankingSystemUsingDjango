from django.contrib import admin
from.models import Currency

# Register your models here.
class CurrencyAdmin(admin.ModelAdmin):
    list_display = ("code","exchange_rate","name")
admin.site.register(Currency,CurrencyAdmin)    
