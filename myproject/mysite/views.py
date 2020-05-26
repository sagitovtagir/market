from django.shortcuts import render
from . import models
from django.http import HttpResponseNotFound


# Create your views here.

def index(request):
    context = {}
    category = models.Category.objects.all()
    category = category.filter(is_active=True)
    context['category'] = category
    return render(request, 'default_template/index.html', context)

def category(request):
    context = {}
    product = models.Product.objects.all()
    product = product.filter(is_active=True)
    category = models.Category.objects.all()
    category = category.filter(is_active=True)
    if 'category' in request.GET:
        category_id = request.GET['category']
        try:
            category_int = int(category_id)
            current_category = category.get(pk=category_int)
            product = product.filter(category__in=current_category.get_descendants(include_self=True))
            context['current_category_name'] = current_category.name
            current_category_ancestors = current_category.get_ancestors(include_self=True)
            context['current_category_ancestors'] = current_category_ancestors
            current_category_children = current_category.get_children()
            context['current_category_children'] = current_category_children
        except:
            return HttpResponseNotFound('Страница не найдена')
    context['product'] = product
    context['category'] = category
    return render(request, 'default_template/category.html', context)

def product(request):
    context = {}
    category = models.Category.objects.all()
    category = category.filter(is_active=True)
    if 'product' in request.GET:
        product_id = request.GET['product']
        try:
            product_int = int(product_id)
            product = models.Product.objects.get(pk=product_int)
            context['product'] = product
            current_category = models.Category.objects.get(pk=product.category_id)
            current_category_ancestors = current_category.get_ancestors(include_self=True)
            context['current_category_ancestors'] = current_category_ancestors
            product_image = models.ProductImage.objects.all().filter(product=product)
            context['product_image'] = product_image
        except:
            return HttpResponseNotFound('Страница не найдена')

    context['category'] = category

    return render(request, 'default_template/product.html', context)
