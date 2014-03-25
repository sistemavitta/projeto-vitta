from django.conf.urls import patterns, include, url


from training.views import TreinosListView

urlpatterns = patterns('training.views',

    #url(r'(?P<pk>\d+)/$', PerfilDetailView.as_view(), name='perfil-detail'),
    url(r'treinos/$', TreinosListView.as_view(), name='list-treinos'),


)
