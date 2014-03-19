from django.shortcuts import render

# Create your views here.
from django.views.generic.base import RedirectView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class HomeRedirectView(RedirectView):

    url= ''

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            self.url = request.user.get_absolute_url()
        return super(HomeRedirectView, self).dispatch(request, *args, **kwargs)




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
