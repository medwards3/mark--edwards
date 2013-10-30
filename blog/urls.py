from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from blog.models import Post
from django.utils import timezone


urlpatterns = patterns('',
	url(r'^$',
        ListView.as_view(
            queryset=Post.objects.order_by('-created')[:5],
            context_object_name='posts',
            template_name='blog/index.html'),
        name='index'),
)