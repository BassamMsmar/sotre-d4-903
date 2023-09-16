from django.urls import path

from .views import ProductList, ProductDetail, BrandList, BrandDetails, queryset_debug
from .api import product_list_api, product_detail_api

urlpatterns = [
    path('', ProductList.as_view(), name='products'),
    path('<str:slug>/', ProductDetail.as_view(), name='product_detail'),

    path('debug', queryset_debug),
    path('api/list', product_list_api),
    path('api/list/<int:product_id>/', product_detail_api),
    
    path('brands', BrandList.as_view(), name='brand_list'), 
    path('brands/<str:slug>', BrandDetails.as_view(), name='brand_details'), 

]