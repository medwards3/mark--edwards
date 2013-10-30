from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.template import Context, loader
from django.http import Http404
from django.core.urlresolvers import reverse
import json
import urllib.request, urllib.error, urllib.parse
from datetime import datetime


