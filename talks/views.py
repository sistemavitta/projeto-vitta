# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.contrib.auth.models import User, Group
from perfil.models import Perfil
from serializers import UserSerializer, GroupSerializer, PerfilSerializer, PesoSerializer, FichaSerializer, TreinosListSerializer,FichaListSerializer, PresencaSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, ListAPIView , UpdateAPIView, CreateAPIView, GenericAPIView
from rest_framework import permissions
from rest_framework.exceptions import ParseError
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from training.models import PesoExercicio
from training.models import Fichas
from training.models import Treinos
from rest_framework import status
from administration.models import Presenca
#import django_filters
#from django.utils.timezone import now
#from rest_framework import filters, viewsets


class UserMixim():

    queryset = User.objects.all().filter(is_active=True)
    serializer_class = UserSerializer
    #permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class UserList(UserMixim,ListAPIView):
    """
    Lista todos usuários.

    Ao passar o parametro '/?username=nome' na url, será aplicado o filtro para buscar o usuário com o nome

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


# class UserDetail(UserMixim,ListAPIView):
#     """
#     Exibe um usuário específico
#     """



'''
class PesoCreate(UpdateAPIView):
    """
        Atualiza o peso de um exercício, senão cria o peso.
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
'''

class PesoCreate(CreateAPIView):
    """
        Criar peso para um exercicio.
    """

    # curl -X PATCH  http://localhost:8000/api/peso/4/ -u admin:123 -d "peso=5321"
    queryset = PesoExercicio.objects.all()
    serializer_class = PesoSerializer

class FichaDetail(ListAPIView):
    """
        Exibe a ficha completa de um usuário

        Passar parametro: ?username=(nome do usuario)

    """

    queryset = Fichas.objects.all().filter(ativo=True)
    serializer_class = FichaSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_queryset(self, *args, **kwargs):
        # Vamos adicionar a possibilidade de filtrar:
        qs = super(FichaDetail, self).get_queryset(*args, **kwargs)

        usuario = self.request.QUERY_PARAMS.get('username')
        if usuario is not None:
            ids=User.objects.all().filter(username__icontains=usuario).values('id')
            lista=[]
            for i in ids:
                lista.append(i.get('id'))
            qs = qs.filter(aluno__in=lista)
            if not qs:
                # Aspecto muito interessante do rest framework, ao levantar
                # certas exceções, ele atribui o código correto, assim como
                # o Http404 do django
                raise ParseError(u'Nenhum usuario encontrado')

        # Poderíamos porém ter usado a api de filtros do rf.
        return qs


class TreinosDetail(APIView):
    """
        Exibe todas fichas do usuario com seus treinos ativos

        se houve parametro (?ultima=true) retorna a ultima ficha ativa


    """

    # queryset = Fichas.objects.all().filter(ativo=True)

    # serializer_class = FichaListSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request,usuario, format=None):
        ultima = self.request.QUERY_PARAMS.get('ultima')
        if ultima:
            ficha= Fichas.objects.all().filter(ativo=True).filter(aluno=usuario).reverse().last()
            #presenca=Presenca.objects.all().filter(aluno=usuario).reverse().last()
            serializer = FichaListSerializer(ficha)
            return Response(serializer.data)
        ficha= Fichas.objects.all().filter(ativo=True).filter(aluno=usuario)
        if not ficha:
            raise ParseError(u'Nenhuma ficha para usuario ')
        serializer = FichaListSerializer(ficha, many=True)
        return Response(serializer.data)

    # def get_queryset(self, *args, **kwargs):
    #     # Vamos adicionar a possibilidade de filtrar:
    #     qs = super(TreinosDetail, self).get_queryset(*args, **kwargs)

    #     usuario = self.request.QUERY_PARAMS.get('usuario')
    #     if usuario is not None:
    #         qs = qs.filter(aluno=usuario)
    #         if not qs:
    #             # Aspecto muito interessante do rest framework, ao levantar
    #             # certas exceções, ele atribui o código correto, assim como
    #             # o Http404 do django
    #             raise ParseError(u'Nenhum usuario encontrado')

    #     # Poderíamos porém ter usado a api de filtros do rf.
    #     return qs
class PresencaDetail(ListAPIView):
    """
        Exibe presenças do usuario

        se houve parametro (?ultima=true) retorna a ultima presenca ativa do usuario

    """


    queryset = Presenca.objects.all()

    serializer_class = PresencaSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    # def get(self, request,usuario, format=None):
    #     ultima = self.request.QUERY_PARAMS.get('ultima')
    #     presencas = Presenca.objects.all().filter(aluno=usuario)
    #     if ultima:
    #         presenca = presencas.reverse().last()
    #         serializer = PresencaSerializer(presenca)
    #         return Response(serializer.data)
    #     if not presencas:
    #         raise ParseError(u'Nenhuma ficha para usuario ')
    #     serializer = PresencaSerializer(presencas, many=True)
    #     return Response(serializer.data)


    def get_queryset(self, *args, **kwargs):
        # Vamos adicionar a possibilidade de filtrar:
        qs = super(PresencaDetail, self).get_queryset(*args, **kwargs)

        usuario = self.request.QUERY_PARAMS.get('username')
        if usuario is not None:
            ids=User.objects.all().filter(username__icontains=usuario).values('id')
            if not ids:
                # Aspecto muito interessante do rest framework, ao levantar
                # certas exceções, ele atribui o código correto, assim como
                # o Http404 do django
                raise ParseError(u'Nenhuma usuario encontrado')
            lista=[]
            for i in ids:
                lista.append(i.get('id'))
            qs = qs.filter(aluno__in=lista)
            if not qs:
                # Aspecto muito interessante do rest framework, ao levantar
                # certas exceções, ele atribui o código correto, assim como
                # o Http404 do django
                raise ParseError(u'Nenhuma presenca para este usuario')

        # Poderíamos porém ter usado a api de filtros do rf.
        return qs



class APIRootView(APIView):
    """
        Navegar pela api Vitta
    """
    def get(self, request):
        data = {

            'get usuarios': reverse('user-list',request=request),
            'create-peso': reverse('peso-create',request=request),
            'get fichas' : reverse('ficha-list', request=request),
            'get presencas' : reverse('presenca-list', request=request),

        }
        return Response(data)
