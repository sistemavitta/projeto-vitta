from administration.models import AdministrationTemp
#from django.contrib.auth.models import User

def context_fichas(request):
    context = {}
    try:
        context['menu']=AdministrationTemp.objects.all().filter(professor=request.user).exclude(aluno=request.user)
    except:
        pass
    return context
