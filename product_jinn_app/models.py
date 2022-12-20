# from django.db import models
from django.contrib.gis.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
import uuid
import pathlib
from django.contrib.auth.models import User

# Create your models here.




class Stores(models.Model):
    store_name = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    coordinates = models.PointField(null=True, blank=True)
    
    def __str__(self):
        return self.store_name
    


class Categories(models.Model):
    title = models.CharField(max_length=50)
    def __str__(self):
        return self.title
    
class Products(models.Model):
    store =  models.ForeignKey(Stores, on_delete=models.DO_NOTHING,related_name="product_store")
    category = models.ForeignKey(Categories, on_delete=models.DO_NOTHING,related_name="product_category")
    created = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(default=0)
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name
    
class Contacts(models.Model):
    store =  models.ForeignKey(Stores, on_delete=models.DO_NOTHING,related_name="contact")
    phone_number = PhoneNumberField(null=False, blank=False, unique=True)
    
    def __str__(self):
        return self.store.store_name +" " + str(self.phone_number)
  
# lets us explicitly set upload path and filename

def upload_to(instance, filename): 
   fpath = pathlib.Path(filename)
   new_fname = str(uuid.uuid1()) #uuid->uuid + timestamp - makes fairly unique urlz
   return f"images/{new_fname}{fpath.suffix}"

class Prod_images(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE,related_name="product_image")
    image_url = models.ImageField(upload_to=upload_to,null=True, blank=True)
    


