from django.shortcuts import render

from django.contrib.auth.models import User, Group
from perfil.models import Perfil
from rest_framework import viewsets
from serializers import UserSerializer, GroupSerializer, PerfilSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PerfilViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows perfil to be viewed or edited.
    """
    queryset = Perfil.objects.all()
    serializer_class = PerfilSerializer