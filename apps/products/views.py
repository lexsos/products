from django.views.generic.base import TemplateView


class ProductView(TemplateView):
    template_name = 'products/products.html'


class EditView(TemplateView):
    template_name = 'products/edit.html'
