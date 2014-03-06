from django.contrib.auth.models import User, Group
from perfil.models import Perfil
from rest_framework import serializers




class PerfilSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Perfil
        fields = ('phone', 'level','image')
        

class UserSerializer(serializers.HyperlinkedModelSerializer):    
    class Meta:
        model = User
        fields = ('id','username', 'first_name','last_name','email', 'groups')
       


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('name')

