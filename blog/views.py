from django.shortcuts import render

# Create your views here.
def home( request ):
	context = { 'title' : 'Blog - Samuel Antonio Gea' }
	return render( request, 'home.html', context )

def posts( request ):
	context = { 'title' : 'Postagens'}
	return render( request, 'posts.html', context )

def sobre( request ):
	context = { 'title' : 'Sobre' }
	return render( request, 'sobre.html', context )

def portfolio( request ):
	context = { 'title' : 'portfolio' }
	return render( request, 'portfolio.html', context )