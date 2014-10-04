from django.conf import settings

from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.core.urlresolvers import reverse_lazy
from django.views.generic import RedirectView


urlpatterns = patterns(
    '',
    url(r'^$', RedirectView.as_view(url=reverse_lazy('view_user_login'))),

    url(r'', include('account.urls')),
    url(r'^database/', include('database.urls')),
    url(r'^weaving/', include('weaving.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('', url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT,
    }),)

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns += staticfiles_urlpatterns()