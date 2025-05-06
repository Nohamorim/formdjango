from django.db import models

SEXO_CHOICES = (
    ('M', 'Masculino'),
    ('F', 'Feminino'),
)

class Cliente(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField(blank=True, null=True)
    sexo = models.CharField(max_length=1, choices=SEXO_CHOICES)
    email = models.EmailField(blank=True, null=True)

    def __str__(self):
        return self.nome