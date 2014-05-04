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
    url(r'^peso/$',views.PesoCreate.as_view(),name='peso-create'),
    url(r'^fichas/$',views.FichaDetail.as_view(),name='ficha-list'),
    url(r'^treinos/(?P<usuario>\d+)/$',views.TreinosDetail.as_view(),name='treinos-detail'),
    url(r'^treino/$',views.TreinoList.as_view(),name='treino-list'),
    url(r'^treino/(?P<pk>\d+)/$',views.TreinoDetail.as_view(),name='treino-detail'),
    url(r'^ficha/$',views.FichaList.as_view(),name='ficha-list'),
    url(r'^ficha/(?P<pk>\d+)/$',views.FichasDetail.as_view(),name='ficha-detail'),
    url(r'^presencas/$',views.PresencaDetail.as_view(),name='presenca-list'),

)
