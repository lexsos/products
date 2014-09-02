import json

from .models import Category, Product, Cost


def getCategoryTree(parent=None, tree_node=None):
    if parent is None:
        tree = []
        for item in Category.objects.filter(parent__isnull=True):
            new_item = {
                'text': item.title,
                'category_pk': item.pk,
            }
            getCategoryTree(item, new_item)
            tree.append(new_item)
        return tree
    else:
        new_nodes = []
        for item in Category.objects.filter(parent=parent):
            new_item = {
                'text': item.title,
                'category_pk': item.pk,
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
            shop_cost = {}
            shop_cost['shop_pk'] = shop.pk
            shop_cost['product_pk'] = product.pk
            shop_cost['price'] = None
            shop_cost['min'] = False
            shop_cost['max'] = False
            item['by_shop'].append(shop_cost)
            if cost:
                shop_cost['price'] = cost[0].price

                if item['min'] is None:
                    item['min'] = shop_cost
                    item['max'] = shop_cost

                if item['min']['price'] > shop_cost['price']:
                    item['min'] = shop_cost
                if item['max']['price'] < shop_cost['price']:
                    item['max'] = shop_cost

        if item['min'] and item['max'] and not (item['min'] is item['max']):
            item['min']['min'] = True
            item['max']['max'] = True

        compare_table.append(item)
    return compare_table
