from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from braces.views import LoginRequiredMixin
from administration.models import AdministrationTemp
from django.views.generic.base import ContextMixin



class PerfilDetailView(LoginRequiredMixin,DetailView):

    template_name = 'perfil/perfil-detail.html'
    model = User
    context_object_name = 'usuario'
    user = None

    def dispatch(self, request, *args, **kwargs):
        self.user = request.user
        return super(PerfilDetailView, self).dispatch(request, *args, **kwargs)


    def get_queryset(self):
        users_admin=AdministrationTemp.objects.all().filter(responsavel=self.user)
        usuarios=[]
        usuarios.append(self.user.pk)
        for i in users_admin.values('usuario'):
            usuarios.append(i.get('usuario'))
        return User.objects.all().filter(pk__in=usuarios)


