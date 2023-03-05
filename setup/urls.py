from django.contrib import admin
from django.urls import path, include
from escola.views import AlunosViewSet, CursosViewSet, MatriculaViewSet, ListaMatriculasAluno, ListaAlunosMatriculados
from rest_framework import routers


# Rota padrão principal
router = routers.DefaultRouter() 

router.register(
    'alunos', AlunosViewSet, 
    basename="Alunos"
    ) # Registrando a rotas /alunos

router.register(
    'cursos', CursosViewSet, 
    basename="Cursos"
    ) # Registrando a rotas /curso

router.register(
    'matriculas', MatriculaViewSet,
    basename="Matriculas"
)




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('aluno/<int:pk>/matriculas/', ListaMatriculasAluno.as_view()),
    path('curso/<int:pk>/matriculas/', ListaAlunosMatriculados.as_view()),
]