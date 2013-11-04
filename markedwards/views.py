from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import Context, loader
from django.http import Http404
from django.core.urlresolvers import reverse
import json
import urllib.request, urllib.error, urllib.parse
from datetime import datetime
from blog.models import Post

def get_json():
	feed = urllib.request.urlopen("https://www.google.com/calendar/feeds/41lp9k24ggd5e2u5no7tmpldlg%40group.calendar.google.com/public/full?orderby=starttime&sortorder=ascending&futureevents=true&alt=json").read()
	return feed

def get_past_json():
	google_date = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")
	feed = urllib.request.urlopen("https://www.google.com/calendar/feeds/41lp9k24ggd5e2u5no7tmpldlg%40group.calendar.google.com/public/full?orderby=starttime&sortorder=descending&start-max={}&alt=json".format(google_date)).read()
	return feed

def json_parse(feed):
	parsed = json.loads(feed.decode("utf8"))
	jlist = []
	for item in parsed['feed']['entry']:
		jitem = {}
		jitem['title'] = item['title']['$t']
		jitem['description'] = item['content']['$t']
		to_parse = item["gd$when"][0]['startTime']
		jitem['time'] = parse_year(to_parse)
		jitem['where'] = item["gd$where"][0]['valueString']
		jlist.append(jitem)
	return jlist

def json_parse_past(feed):
	parsed = json.loads(feed.decode("utf8"))
	jlist = []
	for item in parsed['feed']['entry']:
		jitem = {}
		jitem['title'] = item['title']['$t']
		jitem['description'] = item['content']['$t']
		to_parse = item["gd$when"][0]['startTime']
		jitem['time'] = parse_year(to_parse)
		jitem['where'] = item["gd$where"][0]['valueString']
		jlist.append(jitem)
	return jlist

def json_parse_one(feed):
	parsed = json.loads(feed.decode("utf8"))
	item = parsed['feed']['entry'][0]
	jitem = {}
	jitem['title'] = item['title']['$t']
	jitem['description'] = item['content']['$t']
	to_parse = item["gd$when"][0]['startTime']
	jitem['time'] = parse_year(to_parse)
	jitem['where'] = item["gd$where"][0]['valueString']
	return jitem

def parse_year(ystring):
	# To discard unnecessary info at the end of the string (timezone)
	ylist = ystring.split('+')
	parsed = datetime.strptime(ylist[0], "%Y-%m-%dT%H:%M:%S.000")
	##parsed = datetime.strptime(ystring, "%Y-%m-%dT%H:%M:%S.000+02:00")
	new_time = parsed.strftime("%A %B %d, %H:%M")
	return new_time




def home(request):
	posts = Post.objects.order_by('-created')[:1]
	return render(request, 'home.html', {'posts':posts})

# I used the following code for returning my next concert.
'''def home(request):
	feed = get_json()
	parsed = json_parse_one(feed)
	return render(request, 'home.html', {'event': parsed})
'''

def bio(request):
	return render(request, 'bio.html')

def press(request):
	return render(request, 'press.html',)

def schedule(request):
	feed = get_json()
	parsed = json_parse(feed)
	return render(request, 'schedule.html', {'events': parsed})

def past_schedule(request):
	feed = get_past_json()
	parsed = json_parse_past(feed)
	return render(request, 'past_schedule.html', {'events': parsed})

def programmes(request):
	return render(request, 'programmes.html')

def goldbergs(request):
	return render(request, 'goldbergs.html')

def allemande(request):
	return render(request, 'allemande.html')

def titans(request):
	return render(request, 'titans.html')

def discography(request):
	return render(request, 'discography.html')

def media(request):
	return render(request, 'media.html')

def links(request):
	return render(request, 'links.html')

