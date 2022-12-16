from rest_framework import serializers
from product_jinn_app.models import Stores, Categories, Products, Contacts,Prod_images

class ProductsSerializer(serializers.ModelSerializer):
    #generics dont support changing foreign key values, kit has to be set to read only or a custom update function 
    #created
    # store = serializers.CharField(source='store.store_name')
    # category = serializers.CharField(source='category.title')
    class Meta:
        model= Products
        fields = "__all__"
    # def update(self, instance, validated_data):
        
    #     return super().update(instance, validated_data)
        
class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model= Categories
        fields = "__all__"
        
        
class StoresSerializer(serializers.ModelSerializer):
    class Meta:
        model= Stores
        fields = "__all__"
        
class ContactsSerializer(serializers.ModelSerializer):
    # store = serializers.CharField(source='store.store_name')
    image_url = serializers.ImageField(required=False)
    class Meta:
        model= Contacts
        fields = "__all__"
        
class Prod_imagesSerializer(serializers.ModelSerializer):
    # product = serializers.CharField(source='product.name')
    image_url = serializers.ImageField(required=False)
    class Meta:
        model= Prod_images
        fields = "__all__"
        