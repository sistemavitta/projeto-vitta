from administration.models import AdministrationTemp
from django.core.urlresolvers import resolve
#from django.contrib.auth.models import User

def context_fichas(request):
    context = {}
    try:
        context['menu']=AdministrationTemp.objects.all().filter(professor=request.user).exclude(aluno=request.user)
    except:
        pass
    return context

def resolve_urlname(request):
    """Allows us to see what the matched urlname for this
    request is within the template"""
    try:
        res = resolve(request.path)
        if res:
            return {'urlname' : res.url_name}
    except:
        return {}
