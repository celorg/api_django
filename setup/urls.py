from django.contrib import admin
from django.urls import path, include
from escola.views import AlunosViewsSet, CursosViewSet, MatriculaViewSet, ListaMatriculasAluno, ListaAlunosMatriculados
from rest_framework import routers
from cliente.views import ClientesViewSet

router = routers.DefaultRouter()
router.register('alunos', AlunosViewsSet, basename='Alunos')
router.register('curos', CursosViewSet, basename='Cursos')
router.register('matriculas', MatriculaViewSet, basename='Matriculas')
router.register('clientes', ClientesViewSet, basename='Cliente')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('aluno/<int:pk>/matriculas', ListaMatriculasAluno.as_view()),
    path('curso/<int:pk>/matriculas/', ListaAlunosMatriculados.as_view()),
]
