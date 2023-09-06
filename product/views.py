from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.db.models import Q , F, Value
from django.db.models.aggregates import Max, Min, Sum, Avg
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
    
    

def queryset_debug(request):

    # date = Product.objects.select_related('brand').all() # prefech_releted : with many-to-many

    # filter
    # date = Product.objects.filter(price__gt=70)
    # date = Product.objects.filter(price__lt=70)
    # date = Product.objects.filter(price__lte=70)
    # date = Product.objects.filter(price__range=(70,90))

    # navigate relation
    # date = Product.objects.filter(brand__name='Apple')
    # date = Product.objects.filter(brand__price__lt=20)
    # date = Product.objects.filter(brand__price__lt=20)


    # filter with text 
    # date = Product.objects.filter(name__contains='Brown')
    # date = Product.objects.filter(brand__name__contains='Brown')
    # date = Product.objects.filter(name__endswith ='e')
    # date = Product.objects.filter(name__iendswith='e')
    # date = Product.objects.filter(tags__isnull=False)
    # date = Product.objects.filter(tags__isnull=True)

    #  fiter date time
    # date = Review.objects.filter(create_at__year=2023)
    # date = Review.objects.filter(create_at__month=5)

    # filter 2 values
    # date = Product.objects.filter(price__gt=80, quantity=10) # and
    # date = Product.objects.filter(
    #     Q(price__gt=80) |
    #     Q(quantity=10)
    #     ) # or
    
    # 
    
    # date = Product.objects.filter(
    #     Q(price__gt=80) &
    #     ~Q(quantity=10)
    #     ) # or with not

    # date = Product.objects.filter(price = F('quantity')) # field lookup
    # date = Product.objects.all().order_by('name')
    # date = Product.objects.order_by('name')

    # date = Product.objects.all().order_by('-name')
    # date = Product.objects.order_by('-name') 
    # date = Product.objects.order_by('price', '-name').reverse() 
    # date = Product.objects.all().select_related('brand') # prefech_releted : with many-to-many
    

    # date = Product.objects.order_by('name')[0] 
    # date = Product.objects.order_by('name')[-1]

    # date = Product.objects.earliest('name')
    # date = Product.objects.latest('name')


    # date = Product.objects.latest('name')
    # date = Product.objects.latest('name')


    


    # select columms
    # date = Product.objects.values('name', 'price')
    # date = Product.objects.values('name', 'price', 'brand__name')
    # date = Product.objects.values_list('name', 'price', 'brand__name')

    # remobe duplicate
    # date = Product.objects.all().distinct()
    # date = Product.objects.only('name') # اذا كان في الصفحة متغيرات من خارج المطلوب سوف ياخذ وقت اكبر
    # date = Product.objects.defer('slug') 


    # aggregation

    # date = Product.objects.aggregate(Sum('price')) 
    # date = Product.objects.aggregate(Avg('price')) 


    # annotate
    date = Product.objects.annotate(price_with_tax=F('price')*1.15) 
    date = Product.objects.annotate(price_with_tax=F('price')*1.15) 



    return render(request, 'product/debug.html', {'date':date})
