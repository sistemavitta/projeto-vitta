from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.views.generic.base import RedirectView , View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic.base import ContextMixin
from models import AdministrationTemp
from training.models import Fichas
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.views.generic.base import TemplateResponseMixin
from django.core.urlresolvers import reverse
#return HttpResponseRedirect(reverse('author-detail', kwargs={'pk': self.object.pk}))
#return HttpResponseRedirect('/success/')

class HomeRedirectView(RedirectView):

    url= ''

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            self.url = request.user.get_absolute_url()
        return super(HomeRedirectView, self).dispatch(request, *args, **kwargs)



class AbrirTreinoView(View):

    def post(self, request, *args, **kwargs):

        usuario=get_object_or_404(User.objects.all().filter(is_active=True),pk=request.POST.get('abrir',''))
        if usuario.fichas.count():
            AdministrationTemp.objects.get_or_create(responsavel=request.user,usuario=usuario.pk,ficha=usuario.fichas.count())
            return HttpResponseRedirect(reverse('perfil-detail', kwargs={'pk': usuario.pk}))
        return HttpResponseRedirect('/')


'''
class AbrirTreinoView(TemplateResponseMixin,View,ContextMixin):

    template_name = 'perfil/perfil-detail.html'

    # def get_object(self):
    #     return get_object_or_404(
    #         Fichas,
    #         pk=self.kwargs.get("pk"),
    #     )

    def post(self, request, *args, **kwargs):
        usuario=get_object_or_404(User.objects.all().filter(is_active=True),pk=request.POST.get('abrir',''))
        AdministrationTemp.objects.get_or_create(responsavel=request.user,usuario=usuario.pk,ficha=1 )
        #context = self.get_context_data(**kwargs)
        return HttpResponseRedirect(reverse('perfil-detail', kwargs={'pk': usuario.pk}))
        #return self.render_to_response(context)
        #return render (request,self.template_name, context)

'''




# class AdministrationHomePageView(TemplateView):

#     template_name = "administration/admin-home.html"

#     @method_decorator(login_required)
#     def dispatch(self, *args, **kwargs):
#         return super(AdministrationHomePageView, self).dispatch(*args, **kwargs)

#     '''
#     def get_context_data(self, **kwargs):
#         context = super(HomePageView, self).get_context_data(**kwargs)
#         return context
#     '''
