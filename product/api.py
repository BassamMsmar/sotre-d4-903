from rest_framework.decorators import api_view
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from rest_framework import generics
from .my_filter import PorductFilter
from .serializers import PorductListSerializers, PorductDetailSerializers, BrandListSerializers, BrandDetailSerializers
from .models import Product, Brand

# @api_view(['get'])
# def product_list_api(request):
#     product = Product.objects.all()[:20]
#     date = PorductSerializers(product, many=True, context={'request':request}).data
#     return Response({'product':date})


# @api_view(['get', 'post'])
# def product_detail_api(request, product_id):
#     product = Product.objects.get(id=product_id)
#     date = PorductSerializers(product, context={'request':request}).data
#     return Response({'product':date})


class ProductListApi(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = PorductListSerializers
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['name', 'price','brand']
    search_fields = ['name', 'price']
    ordering_fields = ['name', 'price']
    filterset_class = PorductFilter


class ProductDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = PorductDetailSerializers



class BrandListApi(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandListSerializers


class BrandDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandDetailSerializers