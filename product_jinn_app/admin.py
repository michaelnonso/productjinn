from django.contrib import admin
from product_jinn_app.models import Stores, Categories, Products, Contacts,Prod_images

# Register your models here.
admin.site.register(Stores)
admin.site.register(Categories)
admin.site.register(Products)
admin.site.register(Contacts)
admin.site.register(Prod_images)
