#encoding: utf-8
from django.db import models
from django.contrib.auth.models import User
from filebrowser.fields import FileBrowseField

# Create your models here.
class Perfil(models.Model):

    LEVEL_CHOICES=(
                  (1,u"Administrador"),
                  (2,u"Professor"),
                  (3,u"Aluno"),                                
                  )
    user = models.OneToOneField(User,
                                related_name='perfil')
    image = FileBrowseField(u"Imagem",
    						max_length=200,
    						directory="images/",
    						extensions=[".jpg",".png"],
    						blank=True, null=True)
    phone = models.CharField(u'Telefone', max_length=13)

    level = models.IntegerField(choices=LEVEL_CHOICES,
    						verbose_name=u'Nível')

    def __unicode__(self):
      return unicode(self.user)    

    class Meta:
    	verbose_name=u'Perfil'
    	verbose_name_plural=u'Perfis'


