from django.conf import settings
from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns(
    'account.views',

    url(r'^login/$', 'view_user_login', name='view_user_login'),

)
