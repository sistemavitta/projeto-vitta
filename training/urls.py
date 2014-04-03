from django.conf.urls import patterns, include, url


from training.views import TreinosListView,TreinarView, TreinamentoView

urlpatterns = patterns('training.views',

    #url(r'(?P<pk>\d+)/$', PerfilDetailView.as_view(), name='perfil-detail'),
    url(r'treinos/treinar/(?P<treino>\d+)/$', TreinarView.as_view(), name='iniciar-treinamento'),
    url(r'treinos/$', TreinosListView.as_view(), name='list-treinos'),
    url(r'treinamento/$', TreinamentoView.as_view(), name='treinamento'),


)
