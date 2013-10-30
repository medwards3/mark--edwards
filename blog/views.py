from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import Context, loader
from django.http import Http404
from django.core.urlresolvers import reverse
import json
import urllib.request, urllib.error, urllib.parse
from datetime import datetime
from blog.models import Post

def index(request):
	latest_posts = Post.objects.order_by('-created')[:5]
	return render(request, 'blog/index.html', {'posts':latest_posts})


def post(request, slug):
        # get the Post object
        post = get_object_or_404(Post, slug=slug)
        # now return the rendered template
        return render(request, 'blog/post.html', {'post': post})
