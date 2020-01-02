from django.http import HttpResponse
from django.shortcuts import render
from .models import Product, Category


# index page for products
def products_index(request, category="category"):
    categories = Category.objects.all()
    default_category = Category.objects.get(category_name='Fruits')

    if category != 'category':
        chosen_category = Category.objects.get(category_name=category)
        products = Product.objects.filter(category=chosen_category)
    else:
        products = Product.objects.filter(category=default_category)

    return render(
                    request,
                    'products_index.html',
                      {
                        'products': products,
                        'page_type': 'products',
                        'categories': categories
                      }
                  )


def new(request):
    return HttpResponse('New Products')

