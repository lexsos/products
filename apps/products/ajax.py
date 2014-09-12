from django.utils import simplejson
from dajaxice.decorators import dajaxice_register
from django.template.loader import render_to_string
from django.shortcuts import get_object_or_404

from .utils import getCategoryJson, getProductsCompare
from .models import Shop, Category, Cost, Product


@dajaxice_register
def get_tree(request):
    return getCategoryJson()


@dajaxice_register
def get_compare_table(request, category_pk):
    shop_list = Shop.objects.filter(enabled=True)
    category = Category.objects.get(pk=category_pk)
    context = {
        'category': category,
        'shop_list': shop_list,
        'compare_list': getProductsCompare(category, shop_list)
    }
    body = render_to_string('products/compare_table.html', context)
    return simplejson.dumps({'body': body})


@dajaxice_register
def get_less_compare(request, category_pk):
    category = Category.objects.get(pk=category_pk)
    product_list = category.get_products()
    context = {
        'product_list': product_list,
    }
    body = render_to_string('products/less_compare_list.html', context)
    return simplejson.dumps({'body': body})



@dajaxice_register
def get_edit_table(request, category_pk):
    shop_list = Shop.objects.filter(enabled=True)
    category = Category.objects.get(pk=category_pk)
    context = {
        'category': category,
        'shop_list': shop_list,
        'compare_list': getProductsCompare(category, shop_list)
    }
    body = render_to_string('products/edit_table.html', context)
    return simplejson.dumps({'body': body})


@dajaxice_register
def set_price(request, price, product_pk, shop_pk):
    price = price.replace(',', '.')
    product = get_object_or_404(Product, pk=product_pk)
    shop = get_object_or_404(Shop, pk=shop_pk)
    cost, created = Cost.objects.get_or_create(
        product=product,
        shop=shop,
        defaults={'price': price},
    )
    cost.price = price
    cost.save()