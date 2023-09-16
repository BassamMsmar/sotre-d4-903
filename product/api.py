from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import PorductSerializers
from .models import Product

@api_view()
def product_list_api(request):
    product = Product.objects.all()[:20]
    date = PorductSerializers(product, many=True, context={'request':request}).data
    return Response({'product':date})


@api_view()
def product_detail_api(request, product_id):
    product = Product.objects.get(id=product_id)
    date = PorductSerializers(product, context={'request':request}).data
    return Response({'product':date})