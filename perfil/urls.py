from django.conf.urls import patterns, include, url

from views import PerfilDetailView, AbrirTreinoView

urlpatterns = patterns('perfil.views',

    url(r'abrir/(?P<ficha>\d+)/$', AbrirTreinoView.as_view(), name='abrir-treino'),
    url(r'(?P<pk>\d+)/', include('training.urls')),
    url(r'(?P<pk>\d+)/$', PerfilDetailView.as_view(), name='perfil-detail'),


)
