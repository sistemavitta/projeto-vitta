from django.template import Library
from django.db.models.query import QuerySet

register = Library()
def listpk(menu):
    l = []
    if isinstance(menu, QuerySet):
        for i in menu:
            l.append(i.aluno.pk)
    return str(l)

register.filter('listpk', listpk)
