from django.conf.urls import patterns, include, url


from talks import views

#from rest_framework import routers

'''
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'perfil', views.PerfilViewSet)
'''


urlpatterns = patterns('talks.views',


	url(r'^$',views.APIRootView.as_view()),
    #url(r'^', include(router.urls)),
    url(r'^users/$',views.UserListagem.as_view(),name='user-list'),
    url(r'^user/$',views.UserList.as_view(),name='user-create'),
    url(r'^user/(?P<pk>\d+)/$',views.UserDetail.as_view(),name='user-detail'),
    #url(r'^users/(?P<pk>\d+)/$',views.UserDetail.as_view(),name='user-detail'),
    #url(r'^peso/(?P<pk>\d+)/$',views.PesoCreate.as_view(),name='peso-create'),
    url(r'^peso/$',views.PesoList.as_view(),name='pesoexercicio-list'),
    url(r'^peso/(?P<pk>\d+)/$',views.PesoDetail.as_view(),name='pesoexercicio-detail'),
    url(r'^fichas/$',views.FichaDetail.as_view(),name='ficha-comp'),
    url(r'^treinos/(?P<usuario>\d+)/$',views.TreinosDetail.as_view(),name='treinos-detail2'),
    url(r'^treino/$',views.TreinoList.as_view(),name='treinos-list'),
    url(r'^treino/(?P<pk>\d+)/$',views.TreinoDetail.as_view(),name='treinos-detail'),
    url(r'^ficha/$',views.FichaList.as_view(),name='fichas-list'),
    url(r'^ficha/(?P<pk>\d+)/$',views.FichasDetail.as_view(),name='fichas-detail'),
    url(r'^presencas/$',views.PresencaDetail2.as_view(),name='presenca-lista'),
    url(r'^presenca/$',views.PresencaList.as_view(),name='presenca-list'),
    url(r'^presenca/(?P<pk>\d+)/$',views.PresencaDetail.as_view(),name='presenca-detail'),

    url(r'^nomeexercicio/$',views.NomeExercicioList.as_view(),name='nomesexercicio-list'),
    url(r'^nomeexercicio/(?P<pk>\d+)/$',views.NomeExercicioDetail.as_view(),name='nomesexercicio-detail'),
    url(r'^exercicio/$',views.ExercicioList.as_view(),name='exerciciosaluno-list'),
    url(r'^exercicio/(?P<pk>\d+)/$',views.ExercicioDetail.as_view(),name='exerciciosaluno-detail'),

)
