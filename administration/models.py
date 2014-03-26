#encoding: utf-8

from django.db import models
from django.contrib.auth.models import User
from training.models import Fichas, Treinos

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


    #get_treino_display
    def __unicode__(self):
        return unicode(self.professor)

    class Meta:
        verbose_name_plural=u"AdministrationTemp"
        ordering = ['aberta_em']


