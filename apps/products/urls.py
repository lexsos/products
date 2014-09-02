from django.conf.urls import patterns, url

from .views import (
    category_tree,
    category_edit_tree,
    ProductView,
    CompareTableView,
    EditView,
    EditTableView,
)


urlpatterns = patterns(
    '',
    url(
        r'^$',
        ProductView.as_view(),
        name='products'
    ),
    url(
        r'^edit/$',
        EditView.as_view(),
        name='products_edit'
    ),
    url(
        r'^ajax/tree/$',
        category_tree,
        name='products_tree'
    ),
    url(
        r'^ajax/edit_tree/$',
        category_edit_tree,
        name='category_edit_tree'
    ),
    url(
        r'^ajax/table/(?P<pk>\d+)/$',
        CompareTableView.as_view(),
        name='products_table'
    ),
    url(
        r'^ajax/edit_table/(?P<pk>\d+)/$',
        EditTableView.as_view(),
        name='products_edit_table'
    ),
)
