#encoding: utf-8

from django.db import models
from django.contrib.auth.models import User
from training.models import Fichas, Treinos
from datetime import datetime
from django.utils import timezone

class AdministrationTemp(models.Model):

    professor=models.ForeignKey(User,
                           verbose_name=u"Professor",
                           related_name=u"alunos")
    aluno=models.ForeignKey(User,
                            verbose_name=u'Aluno',
                            related_name=u'professores')
    imagem = models.CharField(verbose_name=u'Imagem',max_length=300)
    ficha=models.ForeignKey(Fichas,
                            verbose_name=u"Ficha",
                            related_name='adminficha',
                            blank=True, null=True)
    aberta_em=models.DateTimeField(verbose_name=u'Aberta em',
                                    auto_now_add=True)
    treino=models.ForeignKey(Treinos,
                             verbose_name=u"Treino",
                             related_name='admintreino',
                             blank=True, null=True)
    treinando=models.BooleanField(verbose_name=u"Treinando?",
                                default=False)
    inicio_treino=models.DateTimeField(verbose_name=u'Início do Treino',null=True, blank=True)

    def duracao(self):
        try:
            intervalo=datetime.utcnow().replace(tzinfo=timezone.utc) - self.inicio_treino
            tempo= (intervalo.days * 24 + intervalo.seconds / 3600.00 + intervalo.microseconds / 3600000000.00 )
        except:
            tempo=0
        #tempo=" %s min" % int(tempo*60)
        return int(tempo*60)
    duracao.short_description=u'Duração'


    def  cronometro(self):
        try:
            intervalo=datetime.utcnow().replace(tzinfo=timezone.utc) - self.inicio_treino
            tempo= (intervalo.days * 24 + intervalo.seconds / 3600.00 + intervalo.microseconds / 3600000000.00 )
        except:
            tempo=0
        #tempo=" %s min" % int(tempo*60)
        return int(tempo*60*60)
    duracao.short_description=u'cronometro'



    #get_treino_display
    def __unicode__(self):
        return unicode(self.professor)

    class Meta:
        verbose_name_plural=u"AdministrationTemp"
        ordering = ['aberta_em']


class Presenca(models.Model):

    aluno=models.ForeignKey(User,
                            verbose_name=u'Aluno',
                            related_name=u'presencas')
    treino=models.ForeignKey(Treinos,
                            verbose_name=u'Treino',
                            related_name=u'treino')
    professor = models.ForeignKey(User,
                                 verbose_name=u'Professor',
                                 related_name='treinamentos')
    data_inicio=models.DateTimeField(verbose_name=u'Data Inicio')
    duracao=models.SmallIntegerField(verbose_name=u'Duração')
    feedback=models.TextField(verbose_name=u"Feedback do Treino",
                               blank=True, null=True)
    ativo=models.BooleanField(verbose_name=u"Ativo",
                              default=True)
    def get_absolute_url(self):
      return "/api/presenca/%i/" % self.id

    def data(self):
        return self.data_inicio


    # def horas(self,dias = 0, horas = 0, minutos = 0, segundos = 0, microssegundos= 0, intervalo = None, tempo = None):
    #     total_horas = dias * 24 + horas + minutos / 60.00 + segundos / 3600.00 + microssegundos / 3600000000.00
    #     if intervalo:
    #         total_horas += intervalo.days * 24 + intervalo.seconds / 3600.00 + intervalo.microseconds / 3600000000.00
    #     if tempo:
    #         total_horas += tempo.hour + tempo.minute / 60.00 + tempo.second /3600.00 + tempo.microsecond / 3600000000.00
    #     return total_horas

    # def duracao(self):
    #     intervalo=self.data_fim - self.data
    #     tempo= (intervalo.days * 24 + intervalo.seconds / 3600.00 + intervalo.microseconds / 3600000000.00 )
    #     tempo=" %s min" % int(tempo*60)
    #     return tempo
    # duracao.short_description=u'Duração'

    def __unicode__(self):
        return unicode(self.data_inicio)

    class Meta:
      verbose_name_plural=u'Presenca dos Alunos'
      ordering=['-data_inicio']

