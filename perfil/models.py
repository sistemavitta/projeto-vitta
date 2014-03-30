#encoding: utf-8
from django.db import models
from django.contrib.auth.models import User
from pyuploadcare.dj import ImageField


class Perfil(models.Model):

    LEVEL_CHOICES=(
                  (1,u"Administrador"),
                  (2,u"Professor"),
                  (3,u"Aluno"),
                  )
    user = models.OneToOneField(User,
                                related_name='perfil')
    image = ImageField(blank=True, null=True, manual_crop="")
    phone = models.CharField(u'Telefone', max_length=13)

    level = models.IntegerField(choices=LEVEL_CHOICES,
    						verbose_name=u'Nível')

    def __unicode__(self):
      return unicode(self.user)

    class Meta:
    	verbose_name=u'Perfil'
    	verbose_name_plural=u'Perfis'


