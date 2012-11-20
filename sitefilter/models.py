from django.db import models


class UserSiteFilter(models.Model):
    user = models.ForeignKey('auth.User')
    sites = models.ManyToManyField('sites.Site')


def get_current_site_filter(request):
    user = request.user
    site_filter, created = UserSiteFilter.objects.get_or_create(user=user)
    return site_filter
