import json
from django.core.urlresolvers import reverse

from .models import Category, Product, Cost


def getCategoryTree(parent=None, tree_node=None):
    if parent is None:
        tree = []
        for item in Category.objects.filter(parent__isnull=True):
            new_item = {
                'text': item.title,
                'url':  reverse('products_table', kwargs={'pk': item.pk}),
            }
            getCategoryTree(item, new_item)
            tree.append(new_item)
        return tree
    else:
        new_nodes = []
        for item in Category.objects.filter(parent=parent):
            new_item = {
                'text': item.title,
                'url':  reverse('products_table', kwargs={'pk': item.pk}),
            }
            getCategoryTree(item, new_item)
            new_nodes.append(new_item)
        if new_nodes:
            tree_node['nodes'] = new_nodes


def getCategoryJson():
    tree = getCategoryTree()
    return json.dumps(tree)


def getProductsCompare(category, shop_list):
    category_list = [item.pk for item in category.get_descendants()]
    category_list.append(category.pk)

    product_list = Product.objects.filter(category__pk__in=category_list)

    compare_table = []

    for product in product_list:
        item = {}
        item['title'] = product.title
        item['min'] = None
        item['max'] = None
        item['by_shop'] = []
        for shop in shop_list:
            cost = Cost.objects.filter(product=product, shop=shop)
            if cost:
                price = cost[0].price
                item['by_shop'].append(price)
                if price > item['max'] or not item['max']:
                    item['max'] = price
                if price < item['min'] or not item['min']:
                    item['min'] = price
            else:
                item['by_shop'].append(None)
        compare_table.append(item)

    return compare_table
