from django.contrib import admin
from .models import Product
class AdminProduct(admin.ModelAdmin):
    list_display=['name','weight','price','created_at','updated_at']

# Register your models here.
admin.site.register(Product, AdminProduct)
