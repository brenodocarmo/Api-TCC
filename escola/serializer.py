from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno # Modelo que será utilizado
        fields = [
            'id', 
            'nome',
            'rg', 
            'cpf',
            'data_nascimento'] 
        # Campos que serão utilizado para API. Podemos escolher quais campos
        # queremos disponibilizar para API


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso 
        fields = '__all__' # Traz todos os campos do Model Curso


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        fields = "__all__"
        # exclude = []


class ListaMatriculasAlunoSerializer(serializers.ModelSerializer) :
    curso = serializers.ReadOnlyField(source='curso.descricao')
    periodo = serializers.SerializerMethodField()
    class Meta:
        model = Matricula
        fields = ['curso', 'periodo']
    
    def get_periodo(self, obj):
        return obj.get_periodo_display()
    

class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source='aluno.nome')
    class Meta:
        model = Matricula
        fields = ['aluno_nome']
