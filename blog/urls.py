from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from blog.models import Post
from django.utils import timezone



urlpatterns = patterns('',
	url(r'^$','blog.views.index', name='index'),
	url(r'^categories/(?P<category>\W*\w*)/$', 'blog.views.categories'),
	url(r'^(?P<slug>[\w\-]+)/$', 'blog.views.post', name='post')
	
)