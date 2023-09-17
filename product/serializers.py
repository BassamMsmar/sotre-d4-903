from rest_framework import serializers
from django.db.models.aggregates import Avg, Aggregate, Count


from .models import Product, Brand

class PorductListSerializers(serializers.ModelSerializer):
    avg_rate = serializers.SerializerMethodField()
    review_count = serializers.SerializerMethodField()
    price_with_tax = serializers.SerializerMethodField()


    class Meta:
        model = Product
        fields = '__all__'

    def get_avg_rate(self, product):
        avg = product.review_product.aggregate(rate_avg=Avg('rate'))
        if not avg['rate_avg']:
            result = 0
            return result
        return avg['rate_avg']
    
    def get_review_count(self, product):
        return product.review_product.count()
    
    def get_price_with_tax(self, product):
        return product.price * 1.15


    



class PorductDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class BrandListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'



class BrandDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'