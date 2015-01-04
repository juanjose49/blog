from django.conf.urls import patterns, include, url
from django.contrib import admin



urlpatterns = patterns('',
    # Examples:
    url(r'^blog/$', 'content.views.blog', name='blog'),
    url(r'^projects/$', 'content.views.projects', name='projects'),
    url(r'^about/$', 'content.views.about', name='about'),
    url(r'^blog/(\d+)/$', 'content.views.blog_entry', name='blog_entry'),
    url(r'^projects/(\d+)/$', 'content.views.projects_entry', name='projects_entry'),


) 

