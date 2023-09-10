from django.shortcuts import render
from django.db.models import Count
from product.models import Brand, Product, Review

# Create your views here.
def home(request): 
    brands = Brand.objects.all().annotate(product_count=Count('product_brand'))[:10]
    sale_product = Product.objects.filter(flag='Sale')[:10]
    feature_product = Product.objects.filter(flag='Feature')[:6]
    new_product = Product.objects.filter(flag='New')[:20]
    reviews = Review.objects.all()

    context = {
        'brands': brands,
        'sale_product': sale_product,
        'new_product': new_product,
        'feature_product': feature_product,
        'reviews': reviews,
    }
    return render(request, 'settings/home.html', context)