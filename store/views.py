from django.shortcuts import render, get_object_or_404
from .models import *


# Create your views here.
def categories(request):
    return {'categories': Category.objects.all()}


def all_products(request):
    products = Product.products.all()
    return render(request, 'store/index.html', {'products': products})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/detail.html', {'product': product})


def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    categories = Category.objects.all()
    products = Product.objects.filter(category=category)

    context = {
        'title': f"Category: {category.title}",
        'category': category,
        'categories': categories,
        'products': products
    }
    sort_fields = request.Get.get('sort')
    if sort_fields:
        context['products'] = context['products'].order_by(*sort_fields)
    return render(request, 'store/base.html', context)


def shop(request):
    return render(request, 'store/shop/shop.html', {})
