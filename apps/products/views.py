from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse

from .utils import getCategoryJson, getProductsCompare
from .models import Category, Shop


def category_tree(request):
    return HttpResponse(
        getCategoryJson('products_table'),
        content_type='application/json',
    )


def category_edit_tree(request):
    return HttpResponse(
        getCategoryJson('products_edit_table'),
        content_type='application/json',
    )


class ProductView(TemplateView):

    template_name = 'products/products.html'

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        context['ajax_tree'] = reverse('products_tree')
        return context


class CompareTableView(DetailView):

    template_name = 'products/compare_table.html'
    model = Category

    def get_context_data(self, **kwargs):
        context = super(CompareTableView, self).get_context_data(**kwargs)
        shop_list = Shop.objects.filter(enabled=True)
        category = context['category']

        context['shop_list'] = shop_list
        context['compare_list'] = getProductsCompare(category, shop_list)
        return context


class EditView(TemplateView):
    template_name = 'products/edit.html'


class EditTableView(DetailView):

    template_name = 'products/edit_table.html'
    model = Category

    def get_context_data(self, **kwargs):
        context = super(EditTableView, self).get_context_data(**kwargs)
        shop_list = Shop.objects.filter(enabled=True)
        category = context['category']

        context['shop_list'] = shop_list
        context['compare_list'] = getProductsCompare(category, shop_list)
        return context
