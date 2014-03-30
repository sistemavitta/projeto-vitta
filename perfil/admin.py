#encoding: utf-8
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from perfil.models import Perfil


# Register your models here.

class PerfilInline(admin.StackedInline):
    model = Perfil
    can_delete = False
    inline_classes = ('grp-collapse grp-open',)
    verbose_name_plural = u'Informações'


class UserAdmin(UserAdmin):

    inlines = (PerfilInline, )
    class Media:
        js = (
            '/static/js/libs/widget.js',
        )


admin.site.unregister(User)
admin.site.register(Perfil)
admin.site.register(User, UserAdmin)
