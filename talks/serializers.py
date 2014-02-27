from django.contrib.auth.models import User, Group
from perfil.models import Perfil
from rest_framework import serializers


class PerfilSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Perfil
        fields = ('url','phone', 'level','image')

class UserSerializer(serializers.HyperlinkedModelSerializer):
	perfil=PerfilSerializer()
	class Meta:
		model = User
		fields = ('url', 'username', 'first_name','last_name','email', 'groups','perfil')


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

