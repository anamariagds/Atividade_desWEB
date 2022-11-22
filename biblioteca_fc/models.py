from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=60)
    matricula = models.CharField(max_length=20)
    curso = models.CharField(max_length=70)

    class Meta: #corrige o nome da classe livros no admin que estava com 's' duplicado
        verbose_name = 'Aluno'
    def __str__(self):
        return self.matricula

class Livro(models.Model):
    titulo = models.CharField(max_length=100)
    autor = models.CharField(max_length=30)
    resumo = models.TextField()

    def __str__(self):
        return self.titulo

class Emprestimo(models.Model):
    titulo = models.ForeignKey(Livro, on_delete=models.CASCADE )
    matricula = models.ForeignKey(Aluno, on_delete=models.CASCADE)
    data_emprestimo = models.DateField(blank = True, null=True)
    data_devolucao = models.DateField(blank = True, null=True)

    def __str__(self):
        return f'{self.matricula} | {self.titulo}'