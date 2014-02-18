# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.views.generic import TemplateView
from administration.views import AdministrationHomePageView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Vitta.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),       

    url(r'^login/',"django.contrib.auth.views.login",
            {'template_name':'core/login.html'},name='login'),

    url(r'^logout/',"django.contrib.auth.views.logout",
            {'next_page':'/'},name='logout'),

    url(r'^core/', include('core.urls')),

    url(r'^administration/', include('administration.urls')),

    url(r'^$', AdministrationHomePageView.as_view(), name='administration-home'),

    # Class-Based Views para renderização de templates

    url(r'^admin-home/$', TemplateView.as_view(template_name='administration/admin-home.html'), name='admin-home'),

    url(r'^admin/', include(admin.site.urls)),
)
