from django.shortcuts import render
from django.views.generic import DetailView
from django.contrib.auth.models import User


class PerfilDetailView(DetailView):

    template_name = 'perfil/perfil-detail.html'
    model = User
    context_object_name = 'user'

    # def get_context_data(self, **kwargs):
    #     context = super(ArticleDetailView, self).get_context_data(**kwargs)
    #     context['now'] = timezone.now()
    #     return context
