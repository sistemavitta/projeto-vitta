#encoding: utf-8

from django.db import models
from django.contrib.auth.models import User



class Fichas(models.Model):

    aluno=models.ForeignKey(User,
                           verbose_name=u"Aluno",
                           related_name=u"fichas")
    objetivo=models.CharField(verbose_name=u"Objetivo do Aluno",
                              max_length=100)
    criado_em=models.DateTimeField(verbose_name=u'Data de Criação',
                                    auto_now_add=True)
    data_inicio=models.DateField(verbose_name=u'Data de Início')
    data_fim=models.DateField(verbose_name=u'Data de Fim')
    ativo=models.BooleanField(verbose_name=u"Ativo",
                              default=True)


    def __unicode__(self):
        return unicode(self.aluno)

    class Meta:
        verbose_name_plural=u"Fichas"
        ordering = ['criado_em']



class TiposTreino(models.Model):

    tipo=models.CharField(verbose_name=u"Tipo de Treino",
                          max_length=50)
    descricao=models.TextField(verbose_name=u'Descrição',
                                blank=True)
    criado_em=models.DateTimeField(verbose_name=u'Data de Criação',
                                    auto_now_add=True)

    def __unicode__(self):
        return unicode(self.tipo)

    class Meta:
        verbose_name_plural=u'Tipo de Treinos'
        ordering=['tipo']



class Treinos(models.Model):

    SERIE_REPETICAO=(
                  (1,"2 x 15"),
                  (2,"3 x 6"),
                  (3,"3 x 8"),
                  (4,"3 x 10"),
                  (5,"3 x 12"),
                  (6,"3 x 15"),
                  (7,"3 x 20"),
                  (8,"3 x 30"),
                  (9,"4 x 6"),
                  (10,"4 x 8"),
                  (11,"4 x 10"),
                  (12,"4 x 12"),
                  (13,"4 x 15"),
                  (14,"4 x 20"),
                  )

    ficha=models.ForeignKey(Fichas,
                            verbose_name=u"Ficha",
                            related_name=u"treinos")
    nome=models.CharField(verbose_name=u"Nome do Treino",
                              max_length=50)
    tipo_treino=models.ForeignKey(TiposTreino,
                           verbose_name=u'Tipo de Treino',
                           related_name=u'treino')
    volume=models.IntegerField(choices=SERIE_REPETICAO,
                                verbose_name="Série/Repetição",
                                blank=True,
                                null=True)
    criado_em=models.DateTimeField(verbose_name=u'Data de Criação',
                                    auto_now_add=True)
    ativo=models.BooleanField(verbose_name=u"Ativo",
                              default=True)


    def __unicode__(self):
        return unicode(self.nome)

    class Meta:
        verbose_name_plural=u'Treinos'
        ordering=['criado_em']



class NomesExercicio(models.Model):

    TIPO_MUSCULO=(
                  (1,u"Abdome"),
                  (2,u"Antebraço"),
                  (3,u"Bíceps"),
                  (4,u"Costas"),
                  (5,u"Coxa"),
                  (6,u"Glúteo"),
                  (7,u"Inferior"),
                  (8,u"Ombro"),
                  (9,u"Panturrilha"),
                  (10,u"Peitoral"),
                  (11,u"Quadríceps"),
                  (12,u"Trapézio"),
                  (13,u"Tríceps"),
                  )
    nome=models.CharField(verbose_name=u"Nome do Exercício",
                          max_length=50)
    musculo=models.IntegerField(choices=TIPO_MUSCULO,
                                verbose_name="Região Muscular")
    criado_em=models.DateTimeField(verbose_name=u'Data de Criação',
                                    auto_now_add=True)
    ativo=models.BooleanField(verbose_name=u"Ativo",
                              default=True)

    def __unicode__(self):
        return unicode(self.nome)

    class Meta:
        verbose_name_plural=u"Nomes dos Exercícios"



class ExerciciosAluno(models.Model):

    treino=models.ForeignKey(Treinos,
                             verbose_name=u"Treino",
                             related_name=u"exercicios")
    #ordem=models.AutoField(verbose_name=u"Ordem")
    nome=models.ForeignKey(NomesExercicio,
                            verbose_name=u"Exercício",
                            related_name=u"exerciciosaluno")
    serie=models.CharField(verbose_name=u"Série",max_length=50,
                              null=True,blank=True )
    repeticao=models.CharField(verbose_name=u"Repetição",max_length=50,
                                  null=True,blank=True)
    criado_em=models.DateTimeField(verbose_name=u'Data de Criação',
                                    auto_now_add=True)
    ativo=models.BooleanField(verbose_name=u"Ativo",
                              default=True)
    my_order = models.PositiveIntegerField(default=0, blank=False, null=False)

    def __unicode__(self):
        return unicode(self.nome)

    class Meta(object):
        verbose_name_plural=u"Exercícios dos Alunos"
        ordering = ['my_order']
        #db_table=u"exercicios"

class PesoExercicio(models.Model):

    exercicio=models.ForeignKey(ExerciciosAluno,
                             verbose_name=u"Exercício",
                             related_name=u"pesos")
    peso=models.SmallIntegerField(verbose_name=u"Peso")
    cadastrado_em=models.DateTimeField(verbose_name=u'Cadastrado em',
                                    auto_now_add=True)
    ativo=models.BooleanField(verbose_name=u"Ativo",
                               default=True)

    def __unicode__(self):
        return unicode(self.peso)

    class Meta:
        verbose_name_plural=u'Pesos Exercícios'
        ordering=['cadastrado_em']
