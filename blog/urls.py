from django.conf.urls import url
from .views import(
	home,
	posts,
	sobre,
	portfolio
)

urlpatterns = [
	url(r'^$', home),
	url(r'^posts/$', posts),
	url(r'^sobre/$', sobre),
	url(r'^portfolio/$', portfolio)
]