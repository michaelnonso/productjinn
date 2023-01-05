from product_jinn_app.api.serializers import (ProductsSerializer
    ,Prod_imagesSerializer
    ,ContactsSerializer
    ,StoresSerializer
    ,CategoriesSerializer)
from product_jinn_app.models import Products, Contacts,Prod_images,Stores, Categories
from product_jinn_app.api import urls
from django.http import JsonResponse

#REST FRAMEWORK IMPORTS
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from product_jinn_app.api.permissions import IsOwnerOrAdminOrReadOnly

from rest_framework.response import Response
from django.urls import get_resolver, get_urlconf




#GenericAPIView watchlist for test search test purposes
class ProductsListG(generics.ListAPIView):         #handles get and post
    queryset = Products.objects.all() #queryset object
    serializer_class = ProductsSerializer
    permission_classes = [IsOwnerOrAdminOrReadOnly]
    
class ProductsDetailG(generics.RetrieveUpdateDestroyAPIView):   #--handles get, put, delete specific products
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = [IsOwnerOrAdminOrReadOnly]
    # #throttle_classes =[UserRateThrottle, AnonRateThrottle]
    # throttle_classes =[ScopedRateThrottle]
    # throttle_scope = 'review-detail'
    
class StoresListG(generics.ListAPIView):         #handles get and post
    queryset = Stores.objects.all() #queryset object
    serializer_class = StoresSerializer
    permission_classes = [IsOwnerOrAdminOrReadOnly]
    
class StoresDetailG(generics.RetrieveUpdateDestroyAPIView):   #--handles get, put, delete specific products
    queryset = Stores.objects.all()
    serializer_class = StoresSerializer
    permission_classes = [IsOwnerOrAdminOrReadOnly]
    
class CategoriesListG(generics.ListAPIView):         #handles get and post
    queryset = Categories.objects.all() #queryset object
    serializer_class = CategoriesSerializer
    permission_classes = [IsOwnerOrAdminOrReadOnly]
    
    
class CategoriesDetailG(generics.RetrieveUpdateDestroyAPIView):   #--handles get, put, delete specific products
    queryset = Categories.objects.all()
    serializer_class = Categories
    permission_classes = [IsOwnerOrAdminOrReadOnly]
    
class ContactsListG(generics.ListAPIView):         #handles get and post
    queryset = Contacts.objects.all() #queryset object
    serializer_class = ContactsSerializer
    permission_classes = [IsOwnerOrAdminOrReadOnly]
    
class ContactsDetailG(generics.RetrieveUpdateDestroyAPIView):   #--handles get, put, delete specific products
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    permission_classes = [IsOwnerOrAdminOrReadOnly]
    
class Prod_imagesListG(generics.ListAPIView):         #handles get and post
    queryset = Prod_images.objects.all() #queryset object
    serializer_class = Prod_imagesSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsOwnerOrAdminOrReadOnly]
    
class Prod_imagesDetailG(generics.RetrieveUpdateDestroyAPIView):   #--handles get, put, delete specific products
    queryset = Prod_images.objects.all()
    serializer_class = Prod_imagesSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsOwnerOrAdminOrReadOnly]
    

# method creates a summary of all endpoints and returns it as a json response
class URLView(APIView):
    def get(self, request):
        return JsonResponse(urls.endpoints)
        
    


