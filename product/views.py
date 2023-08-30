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
        reviews = Review.objects.filter(product=self.get_object())
        context["reviews"] = reviews
        print(reviews)
        print('000000000000000000000000000')
        return context