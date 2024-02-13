from django.contrib import admin
from .models import Order , OrderProduct , Transaction, Discount_Code

admin.site.register(OrderProduct)
admin.site.register(Order)
admin.site.register(Transaction)
admin.site.register(Discount_Code)