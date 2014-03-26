from django.conf.urls import patterns, include, url

from views import PerfilDetailView, AbrirFichaView, FecharFichaView

urlpatterns = patterns('perfil.views',

    url(r'abrir/(?P<ficha>\d+)/$', AbrirFichaView.as_view(), name='abrir-treino'),
    url(r'fechar/(?P<ficha>\d+)/$', FecharFichaView.as_view(), name='fechar-treino'),
    url(r'(?P<pk>\d+)/', include('training.urls')),
    url(r'(?P<pk>\d+)/$', PerfilDetailView.as_view(), name='perfil-detail'),


)
