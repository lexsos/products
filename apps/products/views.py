from django.http import HttpResponse

from .utils import getCategoryJson


def category_tree(request):
    return HttpResponse(
        getCategoryJson(),
        content_type='application/json',
    )
