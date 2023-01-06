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
from rest_framework.permissions import IsAuthenticated

from rest_framework.response import Response
from django.urls import get_resolver, get_urlconf




#GenericAPIView watchlist for test search test purposes
class ProductsListG(generics.ListAPIView):         #handles get and post
    def get_queryset(self):  #method overiding to modify queryset while also having access to request object
        """
        Returns a list of items specific to the authenticated user.
        """
        if self.request.user.is_staff:
            queryset = Products.objects.all() #queryset object
        else:
            queryset = Products.objects.filter(owner=self.request.user.id) #queryset object
        return queryset
    
    serializer_class = ProductsSerializer
    permission_classes = [IsOwnerOrAdminOrReadOnly,IsAuthenticated]
    
class ProductsDetailG(generics.RetrieveUpdateDestroyAPIView):   #--handles get, put, delete specific products
    def get_queryset(self):  #method overiding to modify queryset while also having access to request object
        """
        Returns a list of items specific to the authenticated user.
        """
        if self.request.user.is_staff:
            queryset = Products.objects.all() #queryset object
        else:
            queryset = Products.objects.filter(owner=self.request.user.id) #queryset object
        return queryset
    serializer_class = ProductsSerializer
    permission_classes = [IsOwnerOrAdminOrReadOnly,IsAuthenticated]
    # #throttle_classes =[UserRateThrottle, AnonRateThrottle]
    # throttle_classes =[ScopedRateThrottle]
    # throttle_scope = 'review-detail'
    
class StoresListG(generics.ListAPIView):         #handles get and post
    def get_queryset(self):  #method overiding to modify queryset while also having access to request object
            """
            Returns a list of items specific to the authenticated user.
            """
            if self.request.user.is_staff:
                queryset = Stores.objects.all() #queryset object
            else:
                queryset = Stores.objects.filter(owner=self.request.user.id) #queryset object
            return queryset
    serializer_class = StoresSerializer
    permission_classes = [IsOwnerOrAdminOrReadOnly,IsAuthenticated]
    
class StoresDetailG(generics.RetrieveUpdateDestroyAPIView):   #--handles get, put, delete specific products
    def get_queryset(self):  #method overiding to modify queryset while also having access to request object
            """
            Returns a list of items specific to the authenticated user.
            """
            if self.request.user.is_staff:
                queryset = Stores.objects.all() #queryset object
            else:
                queryset = Stores.objects.filter(owner=self.request.user.id) #queryset object
            return queryset
    serializer_class = StoresSerializer
    permission_classes = [IsOwnerOrAdminOrReadOnly,IsAuthenticated]
    
class CategoriesListG(generics.ListAPIView):         #handles get and post  
    def get_queryset(self):  #method overiding to modify queryset while also having access to request object
            """
            Returns a list of items specific to the authenticated user.
            """
            if self.request.user.is_staff:
                queryset = Categories.objects.all() #queryset object
            else:
                queryset = Categories.objects.filter(owner=self.request.user.id) #queryset object
            return queryset
    serializer_class = CategoriesSerializer
    permission_classes = [IsOwnerOrAdminOrReadOnly,IsAuthenticated]
    
    
class CategoriesDetailG(generics.RetrieveUpdateDestroyAPIView):   #--handles get, put, delete specific products
    def get_queryset(self):  #method overiding to modify queryset while also having access to request object
            """
            Returns a list of items specific to the authenticated user.
            """
            if self.request.user.is_staff:
                queryset = Categories.objects.all() #queryset object
            else:
                queryset = Categories.objects.filter(owner=self.request.user.id) #queryset object
            return queryset
    serializer_class = Categories
    permission_classes = [IsOwnerOrAdminOrReadOnly,IsAuthenticated]
    
class ContactsListG(generics.ListAPIView):         #handles get and post
    def get_queryset(self):  #method overiding to modify queryset while also having access to request object
            """
            Returns a list of items specific to the authenticated user.
            """
            if self.request.user.is_staff:
                queryset = Contacts.objects.all() #queryset object
            else:
                queryset = Contacts.objects.filter(owner=self.request.user.id) #queryset object
            return queryset
    serializer_class = ContactsSerializer
    permission_classes = [IsOwnerOrAdminOrReadOnly,IsAuthenticated]
    
class ContactsDetailG(generics.RetrieveUpdateDestroyAPIView):   #--handles get, put, delete specific products 
    def get_queryset(self):  #method overiding to modify queryset while also having access to request object
            """
            Returns a list of items specific to the authenticated user.
            """
            if self.request.user.is_staff:
                queryset = Contacts.objects.all() #queryset object
            else:
                queryset = Contacts.objects.filter(owner=self.request.user.id) #queryset object
            return queryset
    serializer_class = ContactsSerializer
    permission_classes = [IsOwnerOrAdminOrReadOnly,IsAuthenticated]
    
class Prod_imagesListG(generics.ListAPIView):         #handles get and post
    def get_queryset(self):  #method overiding to modify queryset while also having access to request object
            """
            Returns a list of items specific to the authenticated user.
            """
            if self.request.user.is_staff:
                queryset = Prod_images.objects.all() #queryset object
            else:
                queryset = Prod_images.objects.filter(owner=self.request.user.id) #queryset object
            return queryset
    serializer_class = Prod_imagesSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsOwnerOrAdminOrReadOnly,IsAuthenticated]
    
class Prod_imagesDetailG(generics.RetrieveUpdateDestroyAPIView):   #--handles get, put, delete specific products 
    def get_queryset(self):  #method overiding to modify queryset while also having access to request object
            """
            Returns a list of items specific to the authenticated user.
            """
            if self.request.user.is_staff:
                queryset = Prod_images.objects.all() #queryset object
            else:
                queryset = Prod_images.objects.filter(owner=self.request.user.id) #queryset object
            return queryset
    serializer_class = Prod_imagesSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsOwnerOrAdminOrReadOnly,IsAuthenticated]
    

# method creates a summary of all endpoints and returns it as a json response
class URLView(APIView):
    def get(self, request):
        return JsonResponse(urls.endpoints)
        
    


