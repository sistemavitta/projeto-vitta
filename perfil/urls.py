from django.conf.urls import patterns, include, url

from views import PerfilDetailView

urlpatterns = patterns('perfil.views',

    url(r'(?P<pk>\d+)/$', PerfilDetailView.as_view(), name='perfil-detail'),


)
