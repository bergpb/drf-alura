from rest_framework import serializers
from escola.models import Aluno, Curso


class AlunoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'cpf', 'data_nascimento']


class CursoSerializers(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'