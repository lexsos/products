from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse


class MainPageView(RedirectView):

    permanent = False
    query_string = True

    def get_redirect_url(self):
        return '/tmpl/base.html'
