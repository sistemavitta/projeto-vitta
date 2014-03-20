from administration.models import AdministrationTemp
from django.contrib.auth.models import User

def context_fichas(request):
    context = {}
    context['menu']=AdministrationTemp.objects.all()
    return context
