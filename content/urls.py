from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    url(r'^blog/$', 'content.views.blog', name='blog'),
    url(r'^projects/$', 'content.views.projects', name='projects'),
    url(r'^about/$', 'content.views.about', name='about'),

)
if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns('',
        (r'^img/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}))