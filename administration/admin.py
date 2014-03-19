from django.contrib import admin

from models import AdministrationTemp

class AdministrationTempAdmin(admin.ModelAdmin):
    list_display=['responsavel','usuario','ficha','treino','treinando']
    #search_fields=['aluno__nome']

admin.site.register(AdministrationTemp,AdministrationTempAdmin)
