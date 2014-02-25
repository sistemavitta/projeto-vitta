# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.views.generic import TemplateView
from administration.views import AdministrationHomePageView
from filebrowser.sites import site
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = patterns('',

    (r'^admin/filebrowser/', include(site.urls)),
    (r'^grappelli/', include('grappelli.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # Examples:
    # url(r'^$', 'Vitta.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),     

    url(r'^talks/', include('talks.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^login/',"django.contrib.auth.views.login",
            {'template_name':'core/login.html'},name='login'),

    url(r'^logout/',"django.contrib.auth.views.logout",
            {'next_page':'/'},name='logout'),

    url(r'^core/', include('core.urls')),

    url(r'^administration/', include('administration.urls')),

    url(r'^$', AdministrationHomePageView.as_view(), name='administration-home'),

    # Class-Based Views para renderização de templates

    url(r'^admin-home/$', TemplateView.as_view(template_name='administration/admin-home.html'), name='admin-home'),

    
)

#urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''
if settings.DEBUG:
    # Обработка статичный файлов на сервере разработки
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT, 'show_indexes': True
        }),
        (r'^uploads/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT, 'show_indexes': True
        }),
    )
'''