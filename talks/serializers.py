from django.contrib.auth.models import User, Group
from perfil.models import Perfil
from rest_framework import serializers
from training.models import PesoExercicio
from training.models import Fichas
from training.models import Treinos
from training.models import ExerciciosAluno
from administration.models import Presenca





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






class ExerciciosSerializer(serializers.ModelSerializer):
    peso = serializers.CharField(source='peso')
    class Meta:
        model = ExerciciosAluno
        fields = ('id','nome','serie','repeticao','peso')

class TreinoSerializer(serializers.ModelSerializer):
    #tipo_treino = serializers.CharField(source='get_tipo_treino_display')
    exercicios = ExerciciosSerializer(many=True)
    class Meta:
        model = Treinos
        fields = ('id','nome','tipo_treino','exercicios')

# class UltimaPresenca(serializers.RelatedField):

#     def ultima_presenca(self):
#         return Presenca.objects.all().last()

class FichaSerializer(serializers.ModelSerializer):
    treinos = TreinoSerializer(many=True)
    ultima_presenca = serializers.CharField(source='ultima_presenca')

    class Meta:
        model = Fichas
        fields = ('id','aluno', 'objetivo','criado_em','data_inicio','data_fim','ultima_presenca','treinos')







class TreinosListSerializer(serializers.ModelSerializer):
    #ultima_presenca = serializers.CharField(source='ultima_presenca')

    class Meta:
        model = Treinos
        fields = ('id','nome','criado_em')


# class UltimaListingField(serializers.RelatedField):

#     def to_native(self, value):
#         ultima = Presenca.objects.all().filter(aluno=value.aluno).last()
#         return "ultima"

class FichaListSerializer(serializers.ModelSerializer):
    treinos = TreinosListSerializer(many=True)
    #ultima = UltimaListingField(many=True)
    #criado_em = serializers.DateTimeField()

    class Meta:
        model = Fichas
        fields = ('id','aluno', 'objetivo','criado_em','data_inicio','data_fim','treinos')



class PresencaSerializer(serializers.ModelSerializer):
    #treinonome = TreinoField(many=True)

    class Meta:
        model = Presenca
        fields = ('id', 'aluno','treino','professor','data_inicio','duracao','feedback')
        depth = 1
