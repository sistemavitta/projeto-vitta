from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Vitta.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # Class-based views para renderizar a home do sistema.

    url(r'^$', TemplateView.as_view(template_name='core/login.html'), name='login'),
    url(r'^admin/', include(admin.site.urls)),
)
