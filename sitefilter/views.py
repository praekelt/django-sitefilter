from django.contrib.sites.models import Site
from django.http import Http404, HttpResponseRedirect
from sitefilter.models import get_current_site_filter


def manage(request, id):
    if not request.user.is_staff:
        raise Http404

    sitefilter = get_current_site_filter(request)
    site = Site.objects.get(id=id)

    if site in sitefilter.sites.all():
        sitefilter.sites.remove(site)
    else:
        sitefilter.sites.add(site)

    return HttpResponseRedirect(request.META['HTTP_REFERER'])
