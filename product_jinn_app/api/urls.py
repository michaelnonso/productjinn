
import re
from django.urls import path, include
from rest_framework.routers import DefaultRouter
#from watchlist_app.api.views import movie_list, movie_detail
from product_jinn_app.api.views import (ProductsListG,ProductsDetailG,
                                        ContactsListG,ContactsDetailG,
                                        StoresListG,StoresDetailG,
                                        Prod_imagesListG,Prod_imagesDetailG,
                                        CategoriesListG,CategoriesDetailG)


urlpatterns = [
    path('api/productlist/',ProductsListG.as_view(), name='product-listG'),
    path('api/productlist/<int:pk>/',ProductsDetailG.as_view(), name='product-detail'),
    path('api/storelist/',StoresListG.as_view(), name='store-listG'),
    path('api/storelist/<int:pk>/',StoresDetailG.as_view(), name='store-detail'),
    path('api/contactlist/',ContactsListG.as_view(), name='contact-listG'),
    path('api/contactlist/<int:pk>/',ContactsDetailG.as_view(), name='contact-detail'),
    path('api/categorylist/',CategoriesListG.as_view(), name='category-listG'),
    path('api/categorylist/<int:pk>/',CategoriesDetailG.as_view(), name='category-detail'),
    path('api/product-images/',Prod_imagesListG.as_view(), name='product-images-listG'),
    path('api/product-images/<int:pk>/',Prod_imagesDetailG.as_view(), name='product-images-detail'),
   ]