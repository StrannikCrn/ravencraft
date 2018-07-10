"""Ravencraft URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from app.views import *
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    url(r'^summernote/', include('django_summernote.urls')),
    url(r'^$', index),
    url(r'^nashi-sorta/(?P<group>.+)/(?P<sub_group>.+)', catalog),
    url(r'^gde-kupit/', where_buy),
    url(r'^o-nas/', about_us),
    url(r'^nashi-sorta/', catalog),
    url(r'^get_sorts/(?P<group>.+)/(?P<sub_group>.+)', catalog_ajax),
    url(r'^novosti-i-stati/(?P<url>.+)', news_item),
    url(r'^novosti-i-stati/', news),
    url(r'^get_news/', get_news_block),
    url(r'^kontakty/', contacts),
    url(r'^admin/', admin.site.urls),
	url(r'^robots.txt$', serve, {'path': "/robots.txt", 'document_root': settings.MEDIA_ROOT, 'show_indexes': False}),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
