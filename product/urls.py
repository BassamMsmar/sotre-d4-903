from django.urls import path

from .views import ProductList, ProductDetail, BrandList

urlpatterns = [
    path('', ProductList.as_view(), name='products'),
    path('<str:slug>', ProductDetail.as_view(), name='product_detail'),
    
    path('brands/', BrandList.as_view(), name='brand_list'), 
    path('brands/<str:slug>', BrandList.as_view(), name='brand_details'), 

]