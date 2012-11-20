from django.conf.urls.defaults import patterns, url

urlpatterns = patterns(
    '',
    url(r'^manage/(?P<id>\d+)/$', 'sitefilter.views.manage', name='site_filter'),
)
