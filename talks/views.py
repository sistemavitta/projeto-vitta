# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.contrib.auth.models import User, Group
from perfil.models import Perfil
from serializers import UserSerializer, GroupSerializer, PerfilSerializer, PesoSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, ListAPIView , UpdateAPIView
from rest_framework import permissions
from rest_framework.exceptions import ParseError
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from training.models import PesoExercicio
from rest_framework import status
#import django_filters
#from django.utils.timezone import now
#from rest_framework import filters, viewsets


class UserMixim():

    queryset = User.objects.all().filter(is_active=True)
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserList(UserMixim,ListAPIView):
    """
    Listar todos usuários:

    Ao passar o parametro `username` na url, será aplicado o filtro para buscar o usuário pelo nome

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


class UserDetail(UserMixim,ListAPIView):
    """
    Exibe um usuário específico
    """


class PesoCreate(UpdateAPIView):
    """
        Atualiza o peso de um exercício
    """

    # curl -X PATCH  http://localhost:8000/api/peso/4/ -u admin:123 -d "peso=5321"
    queryset = PesoExercicio.objects.all()
    serializer_class = PesoSerializer

    # def post(self, request, format=None):
    #     serializer = PesoSerializer(data=request.DATA)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class APIRootView(APIView):
    """
        Navegar pela api Vitta
    """
    def get(self, request):
        data = {

            'users': reverse('user-list',request=request),

        }
        return Response(data)
