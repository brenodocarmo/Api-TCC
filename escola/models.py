from django.db import models


class Aluno(models.Model):
    nome = models.CharField(max_length=30)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome
    
class Curso(models.Model):
    NIVEL = (
        ('A', 'Avançado'),
        ('B', 'Básico'),
        ('I', 'Intermediário'),
    )


    codigo_curso = models.CharField(max_length=10)
    descricao = models.CharField(max_length=100)
    nivel = models.CharField(
        max_length=1, 
        choices=NIVEL, 
        blank=False, # Todo curso tem que ter um nivel
        null=False, # Não aceita campo nulo
        default='B'
        )

    def __str__(self):
        return self.descricao


class Matricula(models.Model):
        PERIODO = (
        ('M', 'Matutino'),
        ('V', 'Vespertino'),
        ('N', 'Noturno'),
        )

        aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE)
        curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
        periodo = models.CharField(
        max_length=1, 
        choices=PERIODO, 
        blank=False, # Todo curso tem que ter um nivel
        null=False, # Não aceita campo nulo
        default='M'
        )
