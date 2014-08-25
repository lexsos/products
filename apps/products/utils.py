import json

from .models import Category


def getCategoryTree(parent=None, tree_node=None):
    if parent is None:
        tree = []
        for item in Category.objects.filter(parent__isnull=True):
            new_item = {
                'text': item.title,
                'id': item.pk,
            }
            getCategoryTree(item, new_item)
            tree.append(new_item)
        return tree
    else:
        new_nodes = []
        for item in Category.objects.filter(parent=parent):
            new_item = {
                'text': item.title,
                'id': item.pk,
            }
            getCategoryTree(item, new_item)
            new_nodes.append(new_item)
        if new_nodes:
            tree_node['nodes'] = new_nodes


def getCategoryJson():
    tree = getCategoryTree()
    return json.dumps(tree)
