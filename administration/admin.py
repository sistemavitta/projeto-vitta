from django.contrib import admin

from models import AdministrationTemp, Presenca

class AdministrationTempAdmin(admin.ModelAdmin):
    list_display=['professor','aberta_em','aluno','imagem','ficha','treino','treinando','duracao']
    #search_fields=['aluno__nome']


class PresencaAdmin(admin.ModelAdmin):
    list_display=['data_inicio','duracao','aluno','treino','professor','nota','ativo']


admin.site.register(AdministrationTemp,AdministrationTempAdmin)
admin.site.register(Presenca,PresencaAdmin)
