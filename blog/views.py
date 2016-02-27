from django.shortcuts import render
from django.utils import timezone
from .models import Post, Portfolio

# Create your views here.
def home( request ):
	context = { 'title' : 'Blog - Samuel Antonio Gea' }
	return render( request, 'home.html', context )

def posts( request ):
	posts = Post.objects.filter().order_by('criado')
	context = { 'title' : 'Postagens', 'posts' : posts }
	return render( request, 'posts.html', context )

def sobre( request ):
	context = { 'title' : 'Sobre' }
	return render( request, 'sobre.html', context )

def portfolio( request ):
	context = { 'title' : 'portfolio' }
	return render( request, 'portfolio.html', context )