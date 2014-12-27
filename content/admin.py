from django.contrib import admin
from content.models import PubType, Publication, StaticContent
# Register your models here.

admin.site.register(PubType)
admin.site.register(Publication)
admin.site.register(StaticContent)
