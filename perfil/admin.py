#encoding: utf-8
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from perfil.models import Perfil
from filebrowser.widgets import FileInput

# Register your models here.

class PerfilInline(admin.StackedInline):
    model = Perfil
    can_delete = False    
    inline_classes = ('grp-collapse grp-open',)
    verbose_name_plural = u'Informações'


class UserAdmin(UserAdmin):

    inlines = (PerfilInline, )


admin.site.unregister(User)
#admin.site.register(Perfil)
admin.site.register(User, UserAdmin)