from django.http import HttpResponse
from feed.models import BrainFeeds, ViewerFeed
import json
from django.core import serializers
import dateutil.parser

# Returns k most recent feeds from BrainFeed table.
def return_top_k_feeds(request,extension):
	top_k = int(request.GET.get('k','10')) # default k=10

	viewer_feed = ViewerFeed.objects.all().order_by('id')
	upper_limit = min(len(viewer_feed),top_k)
	viewer_feed = viewer_feed[0:upper_limit]

	viewer_feed_to_json = [x.to_json() for x in viewer_feed]
	return_data = []
	for feeds in viewer_feed_to_json:
		return_data.append(BrainFeeds.objects.filter(id=feeds['feedid'])[0].to_json())
	
	if 'callback' in request.GET:
		# for js response we wrap everything around callback function
		js_response = '%s(%s)'%(request.GET.get('callback'),json.dumps(return_data))
		return HttpResponse(js_response,content_type="application/json")
	else:
		return HttpResponse(json.dumps(return_data),content_type="application/json")

# This function allows infinite scrolling.
def infinite_scrolling(request,extension):
	
	# Feeds already present
	current_feeds = int(request.GET.get('cur','10')) # default cur=10
	
	# Number of extra feeds required
	extra_feeds = int(request.GET.get('k','10')) # default k=10

	viewer_feed = ViewerFeed.objects.all().order_by('id')
	upper_limit = min(len(viewer_feed),current_feeds+extra_feeds)
	viewer_feed = viewer_feed[current_feeds:upper_limit]
	
	viewer_feed_to_json = [x.to_json() for x in viewer_feed]
	return_data = []
	for feeds in viewer_feed_to_json:
		return_data.append(BrainFeeds.objects.filter(id=feeds['feedid'])[0].to_json())
	
	if 'callback' in request.GET:
		# for js response we wrap everything around callback function
		js_response = '%s(%s)'%(request.GET.get('callback'),json.dumps(return_data))
		return HttpResponse(js_response,content_type="application/json")
	else:
		return HttpResponse(json.dumps(return_data),content_type="application/json")

# Filters feeds using the hash word
def filter_feeds_with_hashtags(request,extension):

	hashword = request.GET.get('hashword','null').lower()
	
	brain_feeds = BrainFeeds.objects.filter(toshow=True).filter(hashtags__contains=hashword).order_by('-created_at')
	return_data = []
	for feeds in brain_feeds:
	        return_data.append(feeds.to_json())

	if 'callback' in request.GET:
		# for js response we wrap everything around callback function
		js_response = '%s(%s)'%(request.GET.get('callback'),json.dumps(return_data))
		return HttpResponse(js_response,content_type="application/json")
	else:
		return HttpResponse(json.dumps(return_data),content_type="application/json")

# Filters feeds with types
def filter_feeds_with_type(request,extension):

	_feedtype = request.GET.get('type','null')
	
	brain_feeds = BrainFeeds.objects.filter(toshow=True).filter(feedtype=_feedtype).order_by('-created_at')
	return_data = []
	for feeds in brain_feeds:
	        return_data.append(feeds.to_json())

	if 'callback' in request.GET:
		# for js response we wrap everything around callback function
		js_response = '%s(%s)'%(request.GET.get('callback'),json.dumps(return_data))
		return HttpResponse(js_response,content_type="application/json")
	else:
		return HttpResponse(json.dumps(return_data),content_type="application/json")

# Return feeds created after datetime. Input time should be in ISO string format. It is them parsed to UTC format
def return_feeds_since(request,extension):
	
	time_since = dateutil.parser.parse(request.GET.get('datetime'))	

	brain_feeds = BrainFeeds.objects.filter(toshow=True).filter(created_at__gte=time_since).order_by('-created_at')
	return_data = []
	for feeds in brain_feeds:
	        return_data.append(feeds.to_json())

	if 'callback' in request.GET:
		# for js response we wrap everything around callback function
		js_response = '%s(%s)'%(request.GET.get('callback'),json.dumps(return_data))
		return HttpResponse(js_response,content_type="application/json")
	else:
		return HttpResponse(json.dumps(return_data),content_type="application/json")

# Records upvotes for a feed
def upvotes_recorder(request,extension):

	# @Deedy: Do error handeling if feedid does not exist. Should we return 404?? I'm not sure. 

	feedid = request.GET.get('feedid','null')
	brain_feed = BrainFeeds.objects.get(id=feedid)
	brain_feed.upvotes = brain_feed.upvotes+ 1
	brain_feed.save()
	return_data = []
	return_data.append(brain_feed.to_json())

	if 'callback' in request.GET:
		# for js response we wrap everything around callback function
		js_response = '%s(%s)'%(request.GET.get('callback'),json.dumps(return_data))
		return HttpResponse(js_response,content_type="application/json")
	else:
		return HttpResponse(json.dumps(return_data),content_type="application/json")

