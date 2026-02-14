import datetime
from django.db import models
from django.utils import timezone

class Pergunta(models.Model):
    texto_pergunta = models.CharField(max_length=200)
    data_publicacao = models.DateTimeField("Data de publicação")

    def foi_publicada_recentemente(self):
        return self.data_publicacao >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.texto_pergunta

    class Meta:
        db_table = 'perguntas'

class Opcao(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    texto_opcao = models.CharField(max_length=200)
    votos = models.IntegerField(default=0)

    def __str__(self):
        return self.texto_opcao

    class Meta:
        db_table = "opcoes"
        verbose_name_plural = "Opções"
    
class Comentario(models.Model):
    pergunta = models.ForeignKey(Pergunta, on_delete=models.CASCADE)
    texto_comentario = models.TextField()
    data_hora = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.texto_comentario
    
    class Meta:
        db_table = "comentarios"
        verbose_name_plural = "Comentários"