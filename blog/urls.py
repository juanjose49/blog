from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'content.views.home_page', name='home'),
    url(r'^content/', include('content.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ckeditor/', include('ckeditor.urls')),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)