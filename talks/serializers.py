from django.contrib.auth.models import User, Group
from perfil.models import Perfil
from rest_framework import serializers
from rest_framework import pagination
from training.models import PesoExercicio
from training.models import Fichas
from training.models import Treinos
from training.models import ExerciciosAluno
from training.models import NomesExercicio
from training.models import TiposTreino
from administration.models import Presenca


class LinksSerializer(serializers.Serializer):
    next = pagination.NextPageField(source='*')
    prev = pagination.PreviousPageField(source='*')

class CustomPaginationSerializer(pagination.BasePaginationSerializer):
    links = LinksSerializer(source='*')  # Takes the page object as the source
    total_results = serializers.Field(source='paginator.count')

    results_field = 'objects'

class NomeExercicioGeralLinkSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='nomesexercicio-detail',
    )
    #nome = serializers.CharField(source='get_nome')
    musculo_nome = serializers.CharField(source='get_musculo_display',read_only=True)
    class Meta:
        model=NomesExercicio
        fields = ('id','url','nome','musculo_nome','musculo','ativo')

class TiposTreinoGeralLinkSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='tipostreino-detail',
    )

    class Meta:
        model=TiposTreino
        fields = ('id','url','tipo','descricao')

class ExercicioGeralSerializer(serializers.ModelSerializer):
    #link= serializers.HyperlinkedRelatedField(many=True, view_name='ficha-detail')
    #link = serializers.HyperlinkedIdentityField(view_name='ficha-detail', format='html')
    url = serializers.CharField(source='get_absolute_url', read_only=True)
    class Meta:
        model=ExerciciosAluno

class ExercicioGeralLinkSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='exerciciosaluno-detail',
        format='html'
    )
    nome_exercicio = serializers.CharField(source='get_nome',read_only=True)
    position = serializers.IntegerField(default=0)

    class Meta:
        model=ExerciciosAluno
        fields = ('id','url','treino','nome','nome_exercicio','serie','repeticao','ativo','position')


class TreinoGeralSerializer(serializers.ModelSerializer):
    #tipo_treino = serializers.CharField(source='get_absolute_url')
    #exercicios = ExerciciosSerializer(many=True)
    #track_listing = serializers.HyperlinkedIdentityField(view_name='track-list')
    url = serializers.CharField(source='get_absolute_url', read_only=True)
    class Meta:
        model = Treinos
        #view_name='treino-detail',
        #fields = ('nome','tipo_treino','exercicios','url')
class TreinoGeralLinkSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='treinos-detail',
    )
    exercicios = serializers.HyperlinkedRelatedField(many=True, read_only=True,
                                                 view_name='exerciciosaluno-detail')
    ficha = serializers.HyperlinkedRelatedField(view_name='fichas-detail')
    tipo_treino = serializers.HyperlinkedRelatedField(view_name='tipostreino-detail')
    class Meta:
        model = Treinos
        fields = ('id','url','ficha','nome','tipo_treino','exercicios','volume','ativo','exercicios')

class FichaGeralSerializer(serializers.ModelSerializer):
    #link= serializers.HyperlinkedRelatedField(many=True, view_name='ficha-detail')
    #link = serializers.HyperlinkedIdentityField(view_name='ficha-detail', format='html')
    url = serializers.CharField(source='get_absolute_url', read_only=True)
    class Meta:
        model=Fichas

class FichaGeralLinkSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='fichas-detail',
    )
    treinos = serializers.HyperlinkedRelatedField(many=True, read_only=True,
                                                 view_name='treinos-detail')
    class Meta:
        model=Fichas
        fields = ('id','url','aluno','objetivo','data_inicio','data_fim','ativo','treinos')



class PerfilSerializer(serializers.ModelSerializer):
	level = serializers.CharField(source='get_level_display')
	class Meta:
		model = Perfil
		fields = ('level','image')


class UserCreateSerializer(serializers.ModelSerializer):
    """
        Lista e Cria um usuario
    """
    #url = serializers.CharField(source='get_absolute_url', read_only=True)
    class Meta:
        model = User
        fields = ('id','username', 'email','password')

class UserCreateLinkSerializer(serializers.HyperlinkedModelSerializer):
    """
        Lista e Cria um usuario
    """
    url = serializers.HyperlinkedIdentityField(
        view_name='user-detail',
    )
    fichas = serializers.HyperlinkedRelatedField(many=True, read_only=True,
                                                 view_name='fichas-detail')
    class Meta:
        model = User
        fields = ('id','url','username', 'email','password','is_staff','fichas')

class UserSerializer(serializers.ModelSerializer):
	perfil = PerfilSerializer()

	class Meta:
		model = User
		fields = ('id','username', 'first_name','perfil')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('name')

class PresencaGeralLinkSerializer(serializers.HyperlinkedModelSerializer):
    #link= serializers.HyperlinkedRelatedField(many=True, view_name='ficha-detail')
    #link = serializers.HyperlinkedIdentityField(view_name='ficha-detail', format='html')
    #url = serializers.CharField(source='get_absolute_url', read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='presenca-detail',
    )
    class Meta:
        model=Presenca
        fields=('id','url','aluno','professor','treino','data_inicio','duracao','feedback','ativo')

class PresencaGeralSerializer(serializers.ModelSerializer):
    #link= serializers.HyperlinkedRelatedField(many=True, view_name='ficha-detail')
    #link = serializers.HyperlinkedIdentityField(view_name='ficha-detail', format='html')
    #data_inicio = serializers.DateTimeField(input_formats='%d/%m/%Y')
    url = serializers.CharField(source='get_absolute_url', read_only=True)
    class Meta:
        model=Presenca




class PesoSerializer(serializers.ModelSerializer):

    class Meta:
        model = PesoExercicio
        fields = ('id','exercicio','peso')



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
    #ultima_presenca = serializers.CharField(source='ultima_presenca')

    class Meta:
        model = Fichas
        fields = ('id','aluno', 'objetivo','criado_em','data_inicio','data_fim','treinos')
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
