"""
Proyecto Final
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.urls import re_path as url
from django.conf import settings
from django.views.static import serve
from django.contrib import admin

admin.autodiscover()
admin.site.enable_nav_sidebar = False
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('', include('applications.home.urls')),
    re_path('', include('applications.users.urls')),


    # users app

    url(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
]
