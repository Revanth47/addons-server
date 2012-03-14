from jingo import register
import jinja2

from mkt.site.helpers import new_context
from . import forms


@register.inclusion_tag('search/helpers/search_results.html')
@jinja2.contextfunction
def search_results(context, products, field=None, src=None, dl_src=None):
    src = src or context.get('src')
    dl_src = dl_src or context.get('dl_src', src)
    return new_context(**locals())


@register.function
def SimpleSearchForm(request):
    return forms.SimpleSearchForm(request.GET)
