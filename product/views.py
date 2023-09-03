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


class BrandDetails(DetailView):
    model = Product