from django.conf.urls import patterns, url

from .views import category_tree, ProductView, CompareTableView


urlpatterns = patterns(
    '',
    url(
        r'^$',
        ProductView.as_view(),
        name='products'
    ),
    url(
        r'^ajax/tree/$',
        category_tree,
        name='products_tree'
    ),
    url(
        r'^ajax/table/(?P<pk>\d+)/$',
        CompareTableView.as_view(),
        name='products_table'
    ),
)
