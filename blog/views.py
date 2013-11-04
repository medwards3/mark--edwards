import json
import urllib.request, urllib.error, urllib.parse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.template import Context, loader
from django.http import Http404
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from datetime import datetime
from blog.models import Post, Category
from calendar import month_name



def side_panel(dictionary):
	categories = Category.objects.all()
	dictionary['categories']=categories
	
	now_year = datetime.now().year
	now_month = datetime.now().month
	first = Post.objects.order_by('created')[0]
	first_year = first.created.year
	first_month = first.created.month
	year_dict = {}
	for year in range(first_year, now_year + 1):
		year_dict[year] = []
		for month in range(first_month, 13):
			year_dict[year].append(month_name[month])
			if month == now_month and year == now_year:
				break
		first_month = 1
	dictionary['archive_list'] = year_dict
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
	template_dict = side_panel({'post':post})
	return render(request, 'blog/post.html', template_dict)

def categories(request, category):
	try:
		the_category = Category.objects.get(title=category)
	except:
		return HttpResponseRedirect(reverse('index', urlconf='markedwards.urls'))
	
	posts = Post.objects.filter(categories=the_category)
	posts = pagination(request,posts)
	template_dict = side_panel({'posts':posts})
	return render(request, 'blog/index.html', template_dict)

def archives(request, year, month):
	month = str(list(month_name).index(month))
	posts = Post.objects.filter(created__year=year, created__month=month)
	template_dict = side_panel({'posts':posts})
	return render(request, 'blog/index.html', template_dict)


