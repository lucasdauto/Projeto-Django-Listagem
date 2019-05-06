from django.db import models

# Create your models here.
class Crush (models.Model):

    signo_opcoes = [
        ('aries','áries'),
        ('touro','touro'),
        ('gemios','gemios'),
        ('cancerr','câncer'),
        ('leão','leão'),
        ('virgem','virgem'),
        ('libra','libra'),
        ('escorpiao','escorpião'),
        ('sargitario','sargitario'),
        ('capricornio','capricórnio'),
        ('aquarios','aquários'),
        ('peixes','peixes')
    ]


    nome = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    data = models.DateField()
    signo = models.CharField(max_length=12, choices=signo_opcoes)
    qualidade = models.CharField(max_length=100)
    defeito = models.CharField(max_length=100,default = 'Não está comigo')
    reciproco = models.BooleanField(default=False)
    solteiro = models.BooleanField(default=False)
    foto = models.ImageField(upload_to='',null=True)
    
    def __str__(self):
        return self.nome