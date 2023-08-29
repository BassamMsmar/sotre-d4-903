from django.shortcuts import render
from django.views.generic import ListView, DateDetailView

from .models import Product, Review, Brand

# Create your views here.
class ProductList(ListView):
    model = Product



class ProductDetail(DateDetailView):
    model = Product