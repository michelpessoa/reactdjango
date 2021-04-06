from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'countInStock')
admin.site.register(Review)
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('_id', 'createdAt', 'user')
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)