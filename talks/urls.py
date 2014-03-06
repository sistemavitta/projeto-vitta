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
    url(r'^users/$',views.UserList.as_view(),name='user-list'),
    url(r'^users/(?P<pk>\d+)/$',views.UserDetail.as_view(),name='user-datail'),

)
