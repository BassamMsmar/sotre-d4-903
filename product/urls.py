from django.urls import path

from .views import ProductList, ProductDetail, BrandList, BrandDetails, queryset_depug

urlpatterns = [
    path('', ProductList.as_view(), name='products'),
    path('<str:slug>/', ProductDetail.as_view(), name='product_detail'),
    path('debug', queryset_depug),
    
    path('brands', BrandList.as_view(), name='brand_list'), 
    path('brands/<str:slug>', BrandDetails.as_view(), name='brand_details'), 

]