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
def get_less_detail(request, product_pk):
    product = Product.objects.get(pk=product_pk)
    context = {
        'product': product,
        'cost_list': product.cost_set.order_by('price'),
    }
    body = render_to_string('products/less_compare_detail.html', context)
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


@dajaxice_register
def save_price_list(request, cost_list):

    if not (request.user.is_authenticated() and request.user.is_superuser):
        return simplejson.dumps({'message': 'Need auth'})

    for new_cost in cost_list:
        price = new_cost['price'].replace(',', '.')
        product = get_object_or_404(Product, pk=new_cost['product_pk'])
        shop = get_object_or_404(Shop, pk=new_cost['shop_pk'])
        cost, created = Cost.objects.get_or_create(
            product=product,
            shop=shop,
            defaults={'price': price},
        )
        cost.price = price
        cost.save()
    return simplejson.dumps({'message': 'Save is successfully'})
