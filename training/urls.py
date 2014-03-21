from django.conf.urls import patterns, include, url


from training.views import AbrirTreinoView, TreinosListView

urlpatterns = patterns('training.views',

    #url(r'(?P<pk>\d+)/$', PerfilDetailView.as_view(), name='perfil-detail'),
    url(r'abrir/$', AbrirTreinoView.as_view(), name='abrir-treino'),
    url(r'treinos/(?P<pk>\d+)/$', TreinosListView.as_view(), name='list-treinos'),


)
