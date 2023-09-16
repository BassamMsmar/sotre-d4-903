from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics

from .serializers import PorductSerializers
from .models import Product

@api_view(['get'])
def product_list_api(request):
    product = Product.objects.all()[:20]
    date = PorductSerializers(product, many=True, context={'request':request}).data
    return Response({'product':date})


@api_view(['get', 'post'])
def product_detail_api(request, product_id):
    product = Product.objects.get(id=product_id)
    date = PorductSerializers(product, context={'request':request}).data
    return Response({'product':date})


class ProductListApi(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = PorductSerializers


class ProductDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = PorductSerializers
