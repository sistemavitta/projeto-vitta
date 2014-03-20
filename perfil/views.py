from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator




class PerfilDetailView(DetailView):

    template_name = 'perfil/perfil-home.html'
    model = User
    context_object_name = 'usuario'

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(PerfilDetailView, self).dispatch(request, *args, **kwargs)

    # def get_context_data(self, **kwargs):
    #     context = super(ArticleDetailView, self).get_context_data(**kwargs)
    #     context['now'] = timezone.now()
    #     return context
