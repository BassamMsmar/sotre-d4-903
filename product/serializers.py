from rest_framework import serializers
from django.db.models.aggregates import Avg, Aggregate, Count
from taggit.serializers import (TagListSerializerField,TaggitSerializer)

from .models import Product, Brand, Review




class PorductListSerializers(serializers.ModelSerializer):
    tags = TagListSerializerField()
    brand = serializers.StringRelatedField()
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


class ReviewSerializers(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'


class PorductDetailSerializers(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()
    reviews = ReviewSerializers(source='review_product',many=True)
    avg_rate = serializers.SerializerMethodField()
    review_count = serializers.SerializerMethodField()


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


class BrandListSerializers(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'




class BrandDetailSerializers(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'