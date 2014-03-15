from django.shortcuts import render

# Create your views here.
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


class AdministrationHomePageView(TemplateView):

    template_name = "training/treinos.html"

    @method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(AdministrationHomePageView, self).dispatch(*args, **kwargs)

    '''
    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        return context
    '''