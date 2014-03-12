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
    data_inicio=models.DateTimeField(verbose_name=u'Data de Início')
    data_fim=models.DateTimeField(verbose_name=u'Data de Fim')
    ativo=models.BooleanField(verbose_name=u"Ativo",
                              default=True)

    #get_treino_display
    def __unicode__(self):
        return unicode(self.aluno)

    class Meta:
        verbose_name_plural=u"Fichas"
        ordering = ['criado_em']


class TipoTreino(models.Model):

    tipo=models.CharField(verbose_name=u"Tipo de Treino",
                          max_length=50)
    descricao=models.TextField(verbose_name=u'Descrição',
                                blank=True)
    criado_em=models.DateTimeField(verbose_name=u'Data de Criação',
                                    auto_now_add=True)

    def __unicode__(self):
        return unicode(self.tipo)

    class Meta:
        verbose_name_plural=u'Nome Treino'
        ordering=['tipo']
