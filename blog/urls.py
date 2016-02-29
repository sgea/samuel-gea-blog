from django.conf.urls import url
from .views import(
	home,
	posts,
	post_editar,
	post_create,
	post_detalhe,
	sobre,
	portfolio
)

urlpatterns = [
	url(r'^$', home, name='home' ),
	url(r'^posts/$', posts, name='posts' ),
	url(r'^posts/create/$', post_create, name='post_create' ),
	url(r'^posts/(?P<id>[0-9]+)/$', post_detalhe, name='post_detalhe' ),
	url(r'^posts/(?P<id>[0-9]+)/editar/$', post_editar, name='post_editar' ),
	url(r'^sobre/$', sobre, name='sobre' ),
	url(r'^portfolio/$', portfolio, name='portfolio' )
]