from product_jinn_app.api.serializers import (ProductsSerializer
    ,Prod_imagesSerializer
    ,ContactsSerializer
    ,StoresSerializer
    ,CategoriesSerializer)
from product_jinn_app.models import Products, Contacts,Prod_images,Stores, Categories

#REST FRAMEWORK IMPORTS
from rest_framework import generics
from rest_framework.parsers import MultiPartParser, FormParser


#GenericAPIView watchlist for test search test purposes
class ProductsListG(generics.ListAPIView):         #handles get and post
    queryset = Products.objects.all() #queryset object
    serializer_class = ProductsSerializer
    
class ProductsDetailG(generics.RetrieveUpdateDestroyAPIView):   #--handles get, put, delete specific products
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    # permission_classes = [IsUserReviewerOrAdminOrReadOnly]
    # #throttle_classes =[UserRateThrottle, AnonRateThrottle]
    # throttle_classes =[ScopedRateThrottle]
    # throttle_scope = 'review-detail'
    
class StoresListG(generics.ListAPIView):         #handles get and post
    queryset = Stores.objects.all() #queryset object
    serializer_class = StoresSerializer
    
class StoresDetailG(generics.RetrieveUpdateDestroyAPIView):   #--handles get, put, delete specific products
    queryset = Stores.objects.all()
    serializer_class = StoresSerializer
    
class CategoriesListG(generics.ListAPIView):         #handles get and post
    queryset = Categories.objects.all() #queryset object
    serializer_class = CategoriesSerializer
    
    
class CategoriesDetailG(generics.RetrieveUpdateDestroyAPIView):   #--handles get, put, delete specific products
    queryset = Categories.objects.all()
    serializer_class = Categories
    
class ContactsListG(generics.ListAPIView):         #handles get and post
    queryset = Contacts.objects.all() #queryset object
    serializer_class = ContactsSerializer
    
class ContactsDetailG(generics.RetrieveUpdateDestroyAPIView):   #--handles get, put, delete specific products
    queryset = Contacts.objects.all()
    serializer_class = ContactsSerializer
    
class Prod_imagesListG(generics.ListAPIView):         #handles get and post
    queryset = Prod_images.objects.all() #queryset object
    serializer_class = Prod_imagesSerializer
    parser_classes = (MultiPartParser, FormParser)
    
class Prod_imagesDetailG(generics.RetrieveUpdateDestroyAPIView):   #--handles get, put, delete specific products
    queryset = Prod_images.objects.all()
    serializer_class = Prod_imagesSerializer
    parser_classes = (MultiPartParser, FormParser)
    
