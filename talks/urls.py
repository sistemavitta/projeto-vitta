from django.conf.urls import patterns, include, url

from rest_framework import routers
from talks import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'perfil', views.PerfilViewSet)



urlpatterns = patterns('talks.views',

    #url(r'^$', TemplateView.as_view(template_name='core/base.html'), name='home'),
    url(r'^', include(router.urls)),

)
