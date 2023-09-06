from typing import Iterable, Optional
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.db.models.aggregates import Avg, Aggregate, Count

from taggit.managers import TaggableManager

# Create your models here.

FLAG_TYPES = (
    ('Sale','Sale'),
    ('New','New'),
    ('Feature','Feature'),
 )

class Product(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    flag = models.CharField(_('Falge'), max_length=10, choices=FLAG_TYPES)
    image = models.ImageField(_('Image'), upload_to='products/')
    price = models.IntegerField(_('Price'), )
    sku = models.CharField(_('Sku'), max_length=12)
    subtitle = models.CharField(_('Subtitle'), max_length=300)
    description = models.TextField(_('Description'), max_length=4000)
    quantity = models.IntegerField(_('Quantity'))
    brand = models.ForeignKey('Brand',verbose_name=('Brand'), related_name='product_brand', on_delete=models.CASCADE)
    tags = TaggableManager(_('Tags'))
    slug = models.SlugField(null=True, blank=True)


    # instance method 
    def avg_rate(self):
        avg = self.review_product.aggregate(rate_avg=Avg('rate'))
        if not avg['rate_avg']:
            result = 0
            return result
        return avg['rate_avg']
    
    def count_reviews(self):
        """
        Get the count of reviews for the product.
        
        Returns:
            int: The count of reviews for the product.
        """
        return self.review_product.count()

    def __str__(self) -> str:
            return self.name
        
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)




class ProductImages(models.Model):
    product = models.ForeignKey(Product, verbose_name=('Product Images'), related_name='product_image', on_delete=models.CASCADE)
    images = models.ImageField(_('Images'), upload_to='product_images')

    def __str__(self) -> str:
        return str(self.product)
    



class Brand(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    image = models.ImageField(_('Image'), upload_to='brand') 
    slug = models.SlugField(null=True, blank=True)


    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Brand, self).save(*args, **kwargs)




class Review(models.Model):
    user = models.ForeignKey(User, verbose_name=('User'),  related_name='review_auther', on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, verbose_name=('Product'), related_name='review_product', on_delete=models.CASCADE)
    rate = models.IntegerField(_('Rate'))
    review = models.TextField(_('Review'), max_length=3000)
    create_at = models.DateTimeField(_('Create At'), default=timezone.now)
    
    def __str__(self) -> str:
        return f"{self.user} - {self.product}"