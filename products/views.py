from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


# index page for products
def products_index(request):
    products = Product.objects.all()
    return render(request, 'products_index.html', {'products': products, 'page_type': 'products'})


def new(request):
    return HttpResponse('New Products')

