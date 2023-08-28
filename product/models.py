from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from taggit.managers import TaggableManager

# Create your models here.

FLAG_TYPES = (
    ('Sale','Sale'),
    ('New','New'),
    ('Feature','Feature'),
 )

class Product(models.Model):
    name = models.CharField(max_length=100)
    flag = models.CharField(max_length=10, choices=FLAG_TYPES)
    Image = models.ImageField(upload_to='products')
    price = models.IntegerField()
    sku = models.CharField(max_length=12)
    subtitle = models.CharField(max_length=300)
    description = models.TextField(max_length=4000)
    quantity = models.IntegerField()
    brand = models.ForeignKey('Brand', related_name='product_brand', on_delete=models.CASCADE)
    tags = TaggableManager()
    review = models.ForeignKey('Review', related_name='product_review', on_delete=models.CASCADE)




class Images(models.Model):
    # product = models.ForeignKey(Product, )
    pass



class Brand(models.Model):
    name = models.CharField(max_length=100)
    Image = models.ImageField(upload_to='brand')

    def __str__(self) -> str:
        return self.name



class Review(models.Model):
    user = models.ForeignKey(User, related_name='review_auther', on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, related_name='review_product', on_delete=models.CASCADE)
    rate = models.IntegerField()
    review = models.TextField(max_length=3000)
    create_at = models.DateTimeField(default=timezone.now)
    