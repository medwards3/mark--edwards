from django.conf.urls import patterns, url
from blog.models import Post
from django.utils import timezone



urlpatterns = patterns('',
	url(r'^$','blog.views.index', name='index'),
	url(r'^categories/(?P<category>\W*\w*)/$', 'blog.views.categories', name="categories"),
	url(r'^archives/(?P<year>[0-9]+)/(?P<month>\W*\w*)/$', 'blog.views.archives', name="archives"),
	url(r'^(?P<slug>[\w\-]+)/$', 'blog.views.post', name='post')
	
)