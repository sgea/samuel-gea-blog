from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
	titulo = models.CharField( max_length=150 )
	conteudo = models.TextField()
	autor = models.ForeignKey('auth.User')
	criado = models.DateTimeField( default=timezone.now )
	atualizado = models.DateTimeField( blank=True, null=True )

	def publicar(self):
		self.save()

	def __str__(self):
		return self.titulo

class Portfolio( models.Model ):
	nome_projeto = models.CharField( max_length=100 )
	linguagens = models.CharField( max_length=250 )
	criado = models.DateTimeField( default=timezone.now )
	atualizado = models.DateTimeField( blank=True, null=True )
	link = models.CharField( max_length=250 )

	def __str__( self ):
		return self.nome_projeto