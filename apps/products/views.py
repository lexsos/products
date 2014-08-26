from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.core.urlresolvers import reverse

from .utils import getCategoryJson, getProductsCompare
from .models import Category, Shop


def category_tree(request):
    return HttpResponse(
        getCategoryJson(),
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
