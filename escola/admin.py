from django.contrib import admin
from escola.models import Aluno, Curso, Matricula


class Alunos(admin.ModelAdmin):
    list_display = (
        'id', 
        'nome', 
        'rg', 
        'cpf', 
        'data_nascimento'
        ) # Campos que seráo mostrado no Admim
    list_display_links = (
        'id', 
        'nome'
        ) # Campos que ao clicar podemo altera os dados
    
    search_fields = (
        'nome',
        ) # Campo de busca
    
    list_per_page = 20 # Paginação na quantidade de Dados (20 alunos por páginas)


# Registra a configuração no Admin
admin.site.register(Aluno, Alunos)



class Cursos(admin.ModelAdmin):
    list_display = (
        'id', 
        'codigo_curso', 
        'descricao',
        )
    list_display_links = (
        'id', 
        'codigo_curso'
        )
    search_fields = (
        'codigo_curso',
        )

admin.site.register(Curso, Cursos)


class Matriculas(admin.ModelAdmin):
    list_display = (
        'id', 
        'aluno', 
        'curso',
        'periodo',
        )
    
    list_display_links = (
        'id',
    )

admin.site.register(Matricula, Matriculas)
