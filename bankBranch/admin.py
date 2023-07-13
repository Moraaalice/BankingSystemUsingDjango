from django.contrib import admin
from.models import BankBranch

# Register your models here.
class BankBranchAdmin(admin.ModelAdmin):
    list_display = ("branchName","branchAddress","contactDetails")
admin.site.register(BankBranch,BankBranchAdmin)    
