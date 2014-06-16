from django.shortcuts import get_object_or_404
from django.shortcuts import render
# from django.views.generic import DetailView
# from django.views.generic.base import RedirectView
from django.views.generic.base import View
from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required
# from django.utils.decorators import method_decorator
from braces.views import LoginRequiredMixin
from braces.views import PermissionRequiredMixin
from administration.models import AdministrationTemp
from django.views.generic.base import ContextMixin
from django.views.generic.base import TemplateResponseMixin
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import TemplateView



class ContextalunoMixim(object):

    usuario = None

    def get_context_data(self,**kwargs):
        context = super(ContextalunoMixim, self).get_context_data(**kwargs)
        alunos=AdministrationTemp.objects.all().filter(professor=self.request.user)
        aluno=get_object_or_404(alunos,aluno=self.kwargs.get('pk'))
        context['usuario']= aluno
        self.usuario = aluno
        return context


class LoginAbrirFichaView(LoginRequiredMixin,View):

    def get(self, request, *args, **kwargs):

        aluno=get_object_or_404(User.objects.all().filter(is_active=True),pk=self.kwargs.get('ficha'))
        ficha=aluno.fichas.all().filter(ativo=True).reverse().last()
        try:
            imagem = aluno.perfil.image
        except:
            imagem = "holder.js/43x43/text:-" + aluno.username

        if not AdministrationTemp.objects.all().filter(professor=request.user).filter(aluno=self.kwargs.get('ficha')).exists():
            AdministrationTemp.objects.create(professor=request.user,aluno=aluno,imagem=imagem,ficha=ficha)
        return HttpResponseRedirect(reverse('perfil-detail', kwargs={'pk': aluno.pk}))

class AbrirFichaView(LoginRequiredMixin,PermissionRequiredMixin,View):

    permission_required="administration.open_student"

    def get(self, request, *args, **kwargs):

        aluno=get_object_or_404(User.objects.all().filter(is_active=True),pk=self.kwargs.get('ficha'))
        ficha=aluno.fichas.all().filter(ativo=True).reverse().last()
        try:
            imagem = aluno.perfil.image
        except:
            imagem = "holder.js/43x43/text:-" + aluno.username

        if not AdministrationTemp.objects.all().filter(professor=request.user).filter(aluno=self.kwargs.get('ficha')).exists():
            AdministrationTemp.objects.create(professor=request.user,aluno=aluno,imagem=imagem,ficha=ficha)
        return HttpResponseRedirect(reverse('perfil-detail', kwargs={'pk': aluno.pk}))

class FecharFichaView(LoginRequiredMixin,ContextalunoMixim,View,ContextMixin):

    template_name = 'perfil/perfil-detail.html'

    def get(self, request, *args, **kwargs):
        aluno=get_object_or_404(AdministrationTemp.objects.all().filter(professor=request.user),aluno=self.kwargs.get('pk'))
        if not aluno.treinando:
            aluno.delete()
            if  aluno.aluno.pk == request.user.pk:
                return HttpResponseRedirect(reverse('logout'))
            return HttpResponseRedirect(reverse('perfil-detail', kwargs={'pk': request.user.pk}))

        context = self.get_context_data(**kwargs)
        context['alerta']='Aluno Treinando: Finalize o treinamento para poder fechar a ficha'
        return render (request,self.template_name, context)




class PerfilDetailView(LoginRequiredMixin,ContextalunoMixim,TemplateView):

    #template_name = 'perfil/perfil-detail.html'
    template_name = 'training/list-treinos.html'
    #template_name = 'perfil/mensagens.html'
    #context_object_name = 'usuario'



    # def get_queryset(self):
    #     users_admin=AdministrationTemp.objects.all().filter(professor=self.request.user)
    #     self.user= self.request.user
    #     alunos=[]
    #     alunos.append(self.request.user.pk)
    #     for i in users_admin.values('aluno'):
    #         alunos.append(i.get('aluno'))
    #     return User.objects.all().filter(pk__in=alunos)

    # def get_context_data(self, **kwargs):

    #     context = super(PerfilDetailView, self).get_context_data(**kwargs)
    #     # if self.user.pk == int(self.kwargs.get('pk')):
    #     #     context['admin']={'ficha':0}
    #     #     return context
    #     #context['aluno']=User.objects.get(pk=2)
    #     #context['admin'] = AdministrationTemp.objects.get(aluno=self.kwargs.get('pk'))
    #     context['admin'] = AdministrationTemp.objects.all().filter(professor=self.user.pk).filter(aluno=self.kwargs.get('pk'))[0]
    #     return context


class PresencasListView(LoginRequiredMixin,ContextalunoMixim,TemplateView):

    template_name = 'perfil/list-presencas.html'
