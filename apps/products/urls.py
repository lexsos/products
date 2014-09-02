from django.conf.urls import patterns, url

from .views import (
    ProductView,
    EditView,
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
)
