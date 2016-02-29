from django.shortcuts import render,  redirect, get_object_or_404
from django.utils import timezone
from .models import Post, Portfolio
from .forms import PostForm

# Create your views here.
def home( request ):
	context = { 'title' : 'Blog - Samuel Antonio Gea' }
	return render( request, 'home.html', context )

def posts( request ):
	posts = Post.objects.order_by('-criado')
	context = { 'title' : 'Posts', 'posts' : posts }
	return render( request, 'posts.html', context )

def post_create( request ):
	if request.method == 'POST':
		form = PostForm( request.POST )
		if form.is_valid():
			post = form.save(commit=False)
			post.autor = request.user
			post.criado = timezone.now()
			post.save()
			return redirect('posts')
	else:
		form = PostForm()
	context = { 'title' : 'Criar Post', 'form' : form }
	return render( request, 'post_create.html', context )

def sobre( request ):
	context = { 'title' : 'Sobre' }
	return render( request, 'sobre.html', context )

def portfolio( request ):
	context = { 'title' : 'Portfolio' }
	return render( request, 'portfolio.html', context )

def post_detalhe( request, id ):
	post = get_object_or_404( Post, id=id)
	context = { 'title' : post.titulo, 'post' : post }
	return render( request , 'post_detalhe.html', context )

def post_editar( request, id ):
	post = get_object_or_404( Post, id=id )

	if request.method == 'POST':
		form = PostForm( request.POST, instance=post)
		if form.is_valid():
			post = form.save( commit=False )
			post.autor = request.user
			post.craido = timezone.now()
			post.save()
			return redirect('posts')
	else:
		form = PostForm( instance=post )

	context = { 'title' : 'Editar Post', 'form' : form, 'post' : post }
	return render( request, 'post_editar.html', context)