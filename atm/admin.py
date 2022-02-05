from django.contrib import admin
from . models import customer, register_acc, transaction
# Register your models here.

admin.site.register(customer)
admin.site.register(register_acc)
admin.site.register(transaction)
