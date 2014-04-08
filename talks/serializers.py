from django.contrib.auth.models import User, Group
from perfil.models import Perfil
from rest_framework import serializers
from training.models import PesoExercicio




class PerfilSerializer(serializers.ModelSerializer):
	level = serializers.CharField(source='get_level_display')
	class Meta:
		model = Perfil
		fields = ('level','image')



class UserSerializer(serializers.ModelSerializer):
	perfil = PerfilSerializer()

	class Meta:
		model = User
		fields = ('id','username', 'first_name','perfil')




class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('name')

class PesoSerializer(serializers.ModelSerializer):

    class Meta:
        model = PesoExercicio


