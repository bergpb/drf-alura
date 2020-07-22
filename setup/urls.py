from django.contrib import admin
from django.urls import include, path
from escola.views import AlunosViewSet, CursoViewSet, MatriculaViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('alunos', AlunosViewSet, basename='alunos')
router.register('cursos', CursoViewSet, basename='cursos')
router.register('matriculas', MatriculaViewSet, basename='matriculas')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls))
]
