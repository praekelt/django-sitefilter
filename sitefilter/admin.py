from django.core.exceptions import FieldError
from sitefilter.models import get_current_site_filter


class SiteFilterMixin(object):    
    def queryset(self, request):
        queryset = super(SiteFilterMixin, self).queryset(request)
        sites = get_current_site_filter(request).sites.all()

        if sites:
            try:
                return queryset.filter(site__in=sites).distinct()
            except FieldError:
                return queryset.filter(sites__in=sites).distinct()
            
        return queryset
