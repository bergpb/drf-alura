from rest_framework import viewsets
from escola.models import Aluno, Curso
from escola.serializers import AlunoSerializers, CursoSerializers


class AlunosViewSet(viewsets.ModelViewSet):
    """Exibi todos os alunos e alunas"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializers


class CursoViewSet(viewsets.ModelViewSet):
    """Exibi todos os cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializers