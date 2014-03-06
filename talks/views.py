# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.contrib.auth.models import User, Group
from perfil.models import Perfil
from serializers import UserSerializer, GroupSerializer, PerfilSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, ListAPIView
from rest_framework import permissions
from rest_framework.exceptions import ParseError
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.response import Response

#import django_filters
#from django.utils.timezone import now
#from rest_framework import filters, viewsets

class UserMixim():

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserList(UserMixim,ListAPIView):
    """
    Listar todos usuários:

    Ao passar o parametro `username` na url, sera aplicado o filtro para buscar o usuário pelo nome

    """

    def get_queryset(self, *args, **kwargs):
        # Vamos adicionar a possibilidade de filtrar:
        qs = super(UserList, self).get_queryset(*args, **kwargs)

        search = self.request.QUERY_PARAMS.get('username')
        if search is not None:
            qs = qs.filter(username__icontains=search)
            if not qs:
                # Aspecto muito interessante do rest framework, ao levantar
                # certas exceções, ele atribui o código correto, assim como
                # o Http404 do django
                raise ParseError(u'Nenhum usuario encontrado')

        # Poderíamos porém ter usado a api de filtros do rf.
        return qs


class UserDetail(UserMixim,RetrieveUpdateAPIView):
    """
    Exibe o usuário e permite atualizá-lo
    """



class APIRootView(APIView):
    def get(self, request):
        data = {
            
            'users': reverse('user-list',request=request),
        }
        return Response(data)