from django import template
from django.contrib.sites.models import Site

from sitefilter.models import get_current_site_filter

register = template.Library()


@register.inclusion_tag('sitefilter/sitefilter.html', takes_context=True)
def sitefilter(context):
    site_filter = get_current_site_filter(context['request'])
    
    return {
        'object_list': Site.objects.all(),
        'selected': site_filter.sites.all()
    }
