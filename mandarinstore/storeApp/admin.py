from django.contrib import admin
from storeApp.models import Product,HistoricalCost,Contact
# Register your models here.

admin.site.register(Product)
admin.site.register(HistoricalCost)
admin.site.register(Contact)