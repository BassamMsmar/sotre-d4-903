from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Product, Review, Brand

# Create your views here.
class ProductList(ListView):
    model = Product    #context : object_list, model_list



class ProductDetail(DetailView):
    model = Product

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.filter(product=self.get_object())
        return context



class BrandList(ListView):
    model = Brand    #context : object_list, model_list


class BrandDetails(ListView):
    model = Product
    template_name = 'product/brand_details.html'

    def get_queryset(self):

        # Get the brand based on the slug from the URL kwargs
        brand = Brand.objects.get(slug=self.kwargs['slug'])

        # Filter the queryset to include only entries with the specified brand
        return super().get_queryset().filter(brand=brand)
    

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.get(slug=self.kwargs['slug'])
        return context
    
    