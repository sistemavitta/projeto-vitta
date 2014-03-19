#encoding: utf-8

from django.db import models
from django.contrib.auth.models import User



class AdministrationTemp(models.Model):

    responsavel=models.ForeignKey(User,
                           verbose_name=u"Responsável",
                           related_name=u"menu")
    usuario=models.PositiveSmallIntegerField(verbose_name=u"usuario")
    ficha=models.PositiveSmallIntegerField(verbose_name=u"ficha")
    aberta_em=models.DateTimeField(verbose_name=u'Aberta em',
                                    auto_now_add=True)
    treino=models.PositiveSmallIntegerField(verbose_name=u"treino", blank=True)
    treinando=models.BooleanField(verbose_name=u"Treinando?",
                                default=False)
    inicio_treino=models.DateTimeField(verbose_name=u'Início do Treino')


    #get_treino_display
    def __unicode__(self):
        return unicode(self.responsavel)

    class Meta:
        verbose_name_plural=u"AdministrationTemp"
        ordering = ['aberta_em']


