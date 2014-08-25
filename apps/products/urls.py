from django.conf.urls import patterns, url

from .views import category_tree


urlpatterns = patterns(
    '',
    url(
        r'^$',
        category_tree,
        name='products_tree'
    ),
)
