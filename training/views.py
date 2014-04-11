#encodign: utf-8
from django.shortcuts import render, get_object_or_404

# Create your views here.
# from django.views.generic.base import RedirectView
# from django.views.generic.base import View
# from django.utils.decorators import method_decorator
# from django.contrib.auth.decorators import login_required
# from django.views.generic.base import ContextMixin
# from administration.models import AdministrationTemp
# from training.models import Fichas
# from django.contrib.auth.models import User
# from django.http import HttpResponse
from django.http import HttpResponseRedirect
# from django.views.generic.base import TemplateResponseMixin
from django.core.urlresolvers import reverse
# from django.views.generic.list import ListView
from braces.views import LoginRequiredMixin
from django.views.generic import TemplateView
from perfil.views import ContextalunoMixim
from django.views.generic.base import View
from administration.models import AdministrationTemp
from datetime import datetime
from administration.models import Presenca
#from django.utils.timezone import utc




class TreinosListView(LoginRequiredMixin,ContextalunoMixim,TemplateView):

    #model = Fichas
    template_name = 'training/list-treinos.html'

    # def get_context_data(self,**kwargs):
    #     context = super(TreinosListView, self).get_context_data(**kwargs)
    #     try:
    #         presenca = self.usuario.aluno.presencas.all().reverse().last()
    #     except:
    #         presenca = 0
    #     context['ulpresenca'] = presenca
    #     return context

    # def get(self, request, *args, **kwargs):
    #     self.ficha = request.GET.get('pk','')

    #     return HttpResponse(str(request.GET))
    # def get_context_data(self,**kwargs):
    #     context = super(TreinosListView, self).get_context_data(**kwargs)
    #     # users_admin=AdministrationTemp.objects.all().filter(professor=self.request.user)
    #     # self.user= self.request.user
    #     # alunos=[]
    #     # alunos.append(self.request.user.pk)
    #     # for i in users_admin.values('aluno'):
    #     #     alunos.append(i.get('aluno'))
    #     # self.user = User.objects.all().filter(pk__in=alunos).filter(pk=self.kwargs.get('pk'))[0]
    #     # context['aluno'] = self.user
    #     return context

    # def get_queryset(self):

    #     users_admin=AdministrationTemp.objects.all().filter(professor=self.request.user)
    #     aluno=get_object_or_404(users_admin,aluno=self.kwargs.get('pk'))

    #     if aluno.ficha:
    #         return  Fichas.objects.get(pk=aluno.ficha)
    #     return 0




    # def get_context_data(self, **kwargs):

    #     context = super(TreinosListView, self).get_context_data(**kwargs)
    #     # if self.user.pk == int(self.kwargs.get('pk')):
    #     #     context['admin']={'ficha':0}
    #     #     return context
    #     #context['admin'] = AdministrationTemp.objects.get(aluno=self.kwargs.get('pk'))
    #     context['aluno'] = User.objects.get(pk=self.kwargs.get('pk'))
    #     context['admin'] = AdministrationTemp.objects.all().filter(professor=self.user.pk).filter(aluno=self.kwargs.get('pk'))[0]
    #     return context

    # def get_context_data(self, **kwargs):
    #     context = super(TreinosListView, self).get_context_data(**kwargs)
    #     context['now'] = 'timezone.now()'
    #     return context

class TreinarView(LoginRequiredMixin,View):

    def get(self, request, *args, **kwargs):
        alunos=AdministrationTemp.objects.all().filter(professor=self.request.user)
        aluno=get_object_or_404(alunos,aluno=self.kwargs.get('pk'))
        if not aluno.treinando:
            aluno.treinando = True
            aluno.treino=get_object_or_404(aluno.ficha.treinos,pk=self.kwargs.get('treino'))
            aluno.inicio_treino = datetime.now()
            aluno.save(update_fields=['treino','treinando','inicio_treino'])
        return HttpResponseRedirect(reverse('treinamento', kwargs={'pk': aluno.aluno.pk}))

class FinalizarView(LoginRequiredMixin,View):

    def get(self, request, *args, **kwargs):
        alunos=AdministrationTemp.objects.all().filter(professor=self.request.user)
        aluno=get_object_or_404(alunos,aluno=self.kwargs.get('pk'))
        if aluno.treinando:
            Presenca.objects.create(aluno=aluno.aluno,treino=aluno.treino,professor=aluno.professor,data_inicio=aluno.inicio_treino,duracao=aluno.duracao())
            aluno.treino=None
            aluno.treinando=False
            aluno.inicio_treino= None
            aluno.save(update_fields=['treino','treinando','inicio_treino'])
        return HttpResponseRedirect(reverse('perfil-detail', kwargs={'pk': aluno.aluno.pk}))

class TreinamentoView(LoginRequiredMixin,ContextalunoMixim,TemplateView):

    template_name = 'training/treinamento.html'
