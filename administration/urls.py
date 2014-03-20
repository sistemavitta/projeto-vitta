from django.conf.urls import patterns, include, url

from administration.views import HomeRedirectView,AbrirTreinoView



urlpatterns = patterns('administration.views',

    #url(r'^$', TemplateView.as_view(template_name='core/base.html'), name='home'),
    url(r'^$', HomeRedirectView.as_view(), name='administration-home'),
    url(r'abrir/$', AbrirTreinoView.as_view(), name='abrir-treino'),

)
