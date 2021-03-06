#encoding: utf-8
from django.contrib import admin
from models import Fichas, Treinos , ExerciciosAluno , TiposTreino, NomesExercicio, PesoExercicio

# Register your models here.

class FichasAdmin(admin.ModelAdmin):
    #raw_id_fields = ("aluno",)
    list_display=['pk','aluno','objetivo','criado_em','data_inicio','data_fim','ativo']
    fieldsets=(
               (u'Informações',{'fields':['aluno','objetivo','data_inicio','data_fim','ativo']}),

               )
    search_fields=['aluno__username']
    raw_id_fields = ("aluno",)
    list_filter=['ativo']
    date_hierarchy='criado_em'



class ExerciciosAlunoInline(admin.TabularInline):
    #fields = ("nome","serie","repeticao","position","ativo")
    model=ExerciciosAluno
    sortable_field_name = "position"
    extra=0




class TreinosAdmin(admin.ModelAdmin):
    list_display=['ficha','nome','ativo']
    raw_id_fields = ("ficha",)
    search_fields=['nome']
    search_fields=['ficha']
    #date_hierarchy='data_inicio'
    inlines=[ExerciciosAlunoInline]



class NomesExercicioAdmin(admin.ModelAdmin):
    list_display=['nome','musculo','ativo']
    search_fields=['nome']
    list_filter=['ativo']


class ExerciciosAlunoAdmin(admin.ModelAdmin):
    list_display=['treino','get_nome','serie','repeticao','peso','position','ativo']

    #search_fields=['aluno__nome']
    list_filter=['ativo']
    #inlines=[PesosexerciciosInline]

class PesoExercicioAdmin(admin.ModelAdmin):
    list_display = ['id','exercicio','peso','ativo']

admin.site.register(Fichas,FichasAdmin)
admin.site.register(Treinos,TreinosAdmin)
admin.site.register(NomesExercicio,NomesExercicioAdmin)
admin.site.register(ExerciciosAluno,ExerciciosAlunoAdmin)
admin.site.register(TiposTreino)
admin.site.register(PesoExercicio,PesoExercicioAdmin)
