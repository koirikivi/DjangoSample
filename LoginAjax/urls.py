from django.conf.urls import patterns, include, url
from django.contrib import admin

from userauth.views import *


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'LoginAjax.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', login_page),
    url(r'^login_ajax/', login_ajax),
    url(r'^blog/', blog),
)
