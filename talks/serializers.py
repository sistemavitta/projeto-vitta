from django.contrib.auth.models import User, Group
from perfil.models import Perfil
from rest_framework import serializers
from rest_framework import pagination
from training.models import PesoExercicio
from training.models import Fichas
from training.models import Treinos
from training.models import ExerciciosAluno
from training.models import NomesExercicio
from administration.models import Presenca



class LinksSerializer(serializers.Serializer):
    next = pagination.NextPageField(source='*')
    prev = pagination.PreviousPageField(source='*')

class CustomPaginationSerializer(pagination.BasePaginationSerializer):
    links = LinksSerializer(source='*')  # Takes the page object as the source
    total_results = serializers.Field(source='paginator.count')

    results_field = 'objects'






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



class NomeExercicio(serializers.ModelSerializer):
    musculo = serializers.CharField(source='get_musculo_display')
    class Meta:
        model = NomesExercicio
        fields = ('nome','musculo')


class ExerciciosSerializer(serializers.ModelSerializer):
    peso = serializers.CharField(source='peso')
    nome = NomeExercicio()
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
        depth = 1







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
        depth = 2
