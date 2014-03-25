from django.shortcuts import get_object_or_404
from django.views.generic import DetailView
from django.views.generic.base import RedirectView , View
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from braces.views import LoginRequiredMixin
from administration.models import AdministrationTemp
from django.views.generic.base import ContextMixin
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from braces.views import LoginRequiredMixin



class AbrirTreinoView(LoginRequiredMixin,View):

    def post(self, request, *args, **kwargs):

        usuario=get_object_or_404(User.objects.all().filter(is_active=True),pk=request.POST.get('abrir',''))
        ficha=usuario.fichas.all().filter(ativo=True).last()
        if ficha:
            ficha = ficha.pk
        else:
            ficha = 0
        try:
            imagem = usuario.perfil.image
        except:
            imagem = "holder.js/43x43/text:-" + usuario.username
        AdministrationTemp.objects.get_or_create(responsavel=request.user,usuario=usuario.pk,imagem=imagem,ficha=ficha)
        return HttpResponseRedirect(reverse('perfil-detail', kwargs={'pk': usuario.pk}))




class PerfilDetailView(LoginRequiredMixin,DetailView):

    template_name = 'perfil/perfil-detail.html'
    model = User
    context_object_name = 'usuario'
    user = None

    def get_queryset(self):
        users_admin=AdministrationTemp.objects.all().filter(responsavel=self.request.user)
        self.user= self.request.user
        usuarios=[]
        usuarios.append(self.request.user.pk)
        for i in users_admin.values('usuario'):
            usuarios.append(i.get('usuario'))
        return User.objects.all().filter(pk__in=usuarios)

    # def get_context_data(self, **kwargs):

    #     context = super(PerfilDetailView, self).get_context_data(**kwargs)
    #     # if self.user.pk == int(self.kwargs.get('pk')):
    #     #     context['admin']={'ficha':0}
    #     #     return context
    #     #context['usuario']=User.objects.get(pk=2)
    #     #context['admin'] = AdministrationTemp.objects.get(usuario=self.kwargs.get('pk'))
    #     context['admin'] = AdministrationTemp.objects.all().filter(responsavel=self.user.pk).filter(usuario=self.kwargs.get('pk'))[0]
    #     return context



