from django.contrib.auth.models import User
from django.db import models

class Perfil(models.Model):
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    data_nascimento = models.DateField(
        verbose_name="Data de Nascimento",
        null=True
    )
    genero = models.CharField(max_length=20, null=True)
    endereco = models.CharField(max_length=200, null=False)

    class Meta:
        db_table = "perfis_usuarios"