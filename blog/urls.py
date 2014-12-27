from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'content.views.home_page', name='home'),
    url(r'^content/', include('content.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
