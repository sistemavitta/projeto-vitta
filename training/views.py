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

class AbrirTreinoView(LoginRequiredMixin,View):

    def post(self, request, *args, **kwargs):

        usuario=get_object_or_404(User.objects.all().filter(is_active=True),pk=request.POST.get('abrir',''))
        try:
            imagem = usuario.perfil.image
        except:
            imagem = "holder.js/43x43/text:-" + usuario.username
        AdministrationTemp.objects.get_or_create(responsavel=request.user,usuario=usuario.pk,imagem=imagem,ficha=usuario.fichas.count())
        return HttpResponseRedirect(reverse('perfil-detail', kwargs={'pk': usuario.pk}))



class TreinosListView(ListView):

    model = Fichas
    template_name = 'training/list-treinos.html'
    ficha = None


    # def get(self, request, *args, **kwargs):
    #     self.ficha = request.GET.get('ficha','')

    def get_queryset(self):

        return Fichas.objects.all()


    # def get_context_data(self, **kwargs):
    #     context = super(TreinosListView, self).get_context_data(**kwargs)
    #     context['now'] = 'timezone.now()'
    #     return context
