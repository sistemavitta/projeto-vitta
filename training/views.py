#encodign: utf-8
from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic.base import RedirectView , View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.base import ContextMixin
from administration.models import AdministrationTemp
from training.models import Fichas
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateResponseMixin
from django.core.urlresolvers import reverse
from django.views.generic.list import ListView
from braces.views import LoginRequiredMixin

class ContextUsuarioMixim(object):
    ficha=None

    def get_context_data(self,**kwargs):
        context = super(ContextUsuarioMixim, self).get_context_data(**kwargs)
        users_admin=AdministrationTemp.objects.all().filter(responsavel=self.request.user)
        usuario=get_object_or_404(users_admin,usuario=self.kwargs.get('pk'))
        self.ficha=usuario.ficha
        print self.ficha
        context['usuariomenu']=usuario
        context['usuario']= User.objects.get(pk=usuario.usuario)
        return context




class TreinosListView(ContextUsuarioMixim,ListView):

    #model = Fichas
    template_name = 'training/list-treinos.html'
    context_object_name = 'ficha'


    # def get(self, request, *args, **kwargs):
    #     self.ficha = request.GET.get('pk','')

    #     return HttpResponse(str(request.GET))
    # def get_context_data(self,**kwargs):
    #     context = super(TreinosListView, self).get_context_data(**kwargs)
    #     # users_admin=AdministrationTemp.objects.all().filter(responsavel=self.request.user)
    #     # self.user= self.request.user
    #     # usuarios=[]
    #     # usuarios.append(self.request.user.pk)
    #     # for i in users_admin.values('usuario'):
    #     #     usuarios.append(i.get('usuario'))
    #     # self.user = User.objects.all().filter(pk__in=usuarios).filter(pk=self.kwargs.get('pk'))[0]
    #     # context['usuario'] = self.user
    #     return context

    def get_queryset(self):

        users_admin=AdministrationTemp.objects.all().filter(responsavel=self.request.user)
        usuario=get_object_or_404(users_admin,usuario=self.kwargs.get('pk'))

        if usuario.ficha:
            return  Fichas.objects.get(pk=usuario.ficha)
        return 0




    # def get_context_data(self, **kwargs):

    #     context = super(TreinosListView, self).get_context_data(**kwargs)
    #     # if self.user.pk == int(self.kwargs.get('pk')):
    #     #     context['admin']={'ficha':0}
    #     #     return context
    #     #context['admin'] = AdministrationTemp.objects.get(usuario=self.kwargs.get('pk'))
    #     context['usuario'] = User.objects.get(pk=self.kwargs.get('pk'))
    #     context['admin'] = AdministrationTemp.objects.all().filter(responsavel=self.user.pk).filter(usuario=self.kwargs.get('pk'))[0]
    #     return context

    # def get_context_data(self, **kwargs):
    #     context = super(TreinosListView, self).get_context_data(**kwargs)
    #     context['now'] = 'timezone.now()'
    #     return context
