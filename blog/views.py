from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template import Context, loader
from django.http import Http404
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import json
import urllib.request, urllib.error, urllib.parse
from datetime import datetime
from blog.models import Post, Category

def side_panel(dictionary):
	categories = Category.objects.all()
	dictionary['categories']=categories
	return dictionary


def pagination(request, posts):
	paginator = Paginator(posts, 5)
	page = request.GET.get('page')
	
	try:
		posts = paginator.page(page)

	except PageNotAnInteger:
		posts = paginator.page(1)
	
	except EmptyPage:
		#If the page is out of range, deliver last page of results.
		posts = paginator.page(paginator.num_pages)
	return posts

def index(request):
	posts = Post.objects.all()
	posts = pagination(request,posts)
	template_dict = side_panel({'posts':posts})
	return render(request, 'blog/index.html', template_dict)


def post(request, slug):
    # get the Post object
    post = get_object_or_404(Post, slug=slug)
    # now return the rendered template
    return render(request, 'blog/post.html', {'post': post})

def categories(request, category):
	'''try:
		the_category = Category.objects.get(title=category)
	except:
		return HttpResponseRedirect(reverse('index', urlconf='markedwards.urls'))'''
	return HttpResponseRedirect(reverse('index', urlconf='markedwards.urls'))
	posts = Post.objects.filter(title=the_category)
	posts = pagination(request,posts)
	template_dict = side_panel({'posts':posts})
	return render(request, 'blog/index.html', template_dict)

