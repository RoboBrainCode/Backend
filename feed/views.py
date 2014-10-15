from django.http import HttpResponse
from feed.models import BrainFeeds, ViewerFeed
import json
import numpy as np
from django.core import serializers
import dateutil.parser
from django.views.decorators.csrf import ensure_csrf_cookie
from django.db.transaction import commit_on_success

# Returns k most recent feeds from BrainFeed table.
def return_top_k_feeds(request):
    # Number of feeds required
    top_k = int(request.GET.get('k','10')) # default k=10

    max_len = ViewerFeed.objects.count()
    upper_limit = min(max_len, top_k)

    feed_ids = list(ViewerFeed.objects.values_list('feedid', flat=True).order_by('id')[:upper_limit])

    brainfeeds_db = BrainFeeds.objects.filter(id__in=feed_ids)

    # Reordering brainfeeds from the DB in order of feed_ids in O(n)
    # s.t. feed_ids == [bf.id for bf in brainfeeds]
    feed_map_order = {feed_ids[i] : i for i in xrange(len(feed_ids))}
    brainfeeds = [0]  * len(feed_ids)
    for bf in list(brainfeeds_db):
        brainfeeds[feed_map_order[bf.id]] = bf

    update_scores_top_k(brainfeeds)
    json_feeds = [feed.to_json() for feed in brainfeeds]

    return HttpResponse(json.dumps(json_feeds), content_type="application/json")


# This function allows infinite scrolling.
def infinite_scrolling(request):

    # Feeds already present
    current_feeds = int(request.GET.get('cur','10')) # default cur=10

    # Number of extra feeds required
    extra_feeds = int(request.GET.get('k','10')) # default k=10

    max_len = ViewerFeed.objects.count()
    upper_limit = min(max_len, current_feeds + extra_feeds)

    feed_ids = list(ViewerFeed.objects.values_list('feedid', flat=True).order_by('id')[current_feeds:upper_limit])

    brainfeeds_db = BrainFeeds.objects.filter(id__in=feed_ids)

    # Reordering brainfeeds from the DB in order of feed_ids in O(n)
    # s.t. feed_ids == [bf.id for bf in brainfeeds]
    feed_map_order = {feed_ids[i] : i for i in xrange(len(feed_ids))}
    brainfeeds = [0]  * len(feed_ids)
    for bf in list(brainfeeds_db):
        brainfeeds[feed_map_order[bf.id]] = bf

    update_scores_scroll(brainfeeds, current_feeds, extra_feeds)
    json_feeds = [feed.to_json() for feed in brainfeeds]

    return HttpResponse(json.dumps(json_feeds), content_type="application/json")

@commit_on_success
def update_scores_top_k(brainfeeds):
    for feeds in brainfeeds:
        feeds.update_score = True
        feeds.log_normalized_feed_show += 1.0
        feeds.save()

@commit_on_success
def update_scores_scroll(brainfeeds, current_feeds, extra_feeds):
    page_number = current_feeds/max(1.0,extra_feeds) + 1.0
    for feeds in brainfeeds:
        feeds.update_score = True
        feeds.log_normalized_feed_show += np.log10(1.0+page_number)
        feeds.save()

# Filters feeds using the hash word
def filter_feeds_with_hashtags(request):

    hashword = request.GET.get('hashword')

    # Number of extra feeds required
    k = int(request.GET.get('k','10')) # default k=10

    if not hashword:
        error_response = {
            'Error': 'hashword not provided.'
        }
        return HttpResponse(json.dumps(error_response), content_type='application/json')

    brain_feeds = BrainFeeds.objects.filter(toshow=True).filter(hashtags__contains=hashword).order_by('-created_at')[:k]
    json_feeds = [feed.to_json() for feed in brain_feeds]
    return HttpResponse(json.dumps(json_feeds), content_type="application/json")

# Filters feeds with types
def filter_feeds_with_type(request):

    feedtype = request.GET.get('type')
    print(feedtype)
    # Number of extra feeds required
    k = int(request.GET.get('k','10')) # default k=10

    if not feedtype:
        error_response = {
            'Error': 'type not provided.'
        }
        return HttpResponse(json.dumps(error_response), content_type='application/json')

    brain_feeds = BrainFeeds.objects.filter(toshow=True).filter(source_text=feedtype).order_by('-created_at')[:k]
    json_feeds = [feed.to_json() for feed in brain_feeds]
    return HttpResponse(json.dumps(json_feeds), content_type="application/json")


# Return feeds created after datetime. Input time should be in ISO string format. It is them parsed to UTC format
def return_feeds_since(request):

    time_since = dateutil.parser.parse(request.GET.get('datetime'))

    # Number of extra feeds required
    k = int(request.GET.get('k','10')) # default k=10

    if not time_since:
        error_response = {
            'Error': 'time_since not provided.'
        }
        return HttpResponse(json.dumps(error_response), content_type='application/json')

    brain_feeds = BrainFeeds.objects.filter(toshow=True).filter(created_at__gte=time_since).order_by('-created_at')[:k]
    json_feeds = [feed.to_json() for feed in brain_feeds]
    return HttpResponse(json.dumps(json_feeds), content_type="application/json")

# Records upvotes for a feed
@ensure_csrf_cookie
def upvotes_recorder(request):
    if request.method == 'GET':
        return HttpResponse('Ok')
    elif request.method == 'POST':
        payload = json.loads(request.body)
        feedid = payload['feedid']
        vote_dir = payload['vote']
        change = payload['change']

        if not feedid:
            error_response = {
                'Error': 'No feedid provided'
            }
            return HttpResponse(json.dumps(error_response), content_type='application/json')
        if not vote_dir == -1 and not vote_dir == 1:
            error_response = {
                'Error': 'voteid {0} not provided. Can only be 1 or -1'.format(vote_dir)
            }
            return HttpResponse(json.dumps(error_response), content_type='application/json')

        brain_feed = BrainFeeds.objects.get(id=feedid)
        votes = {}
        if vote_dir == 1:
            brain_feed.upvotes += 1
            if change:
                brain_feed.downvotes -= 1
        if vote_dir == -1:
            brain_feed.downvotes += 1
            if change:
                brain_feed.upvotes -= 1
        votes = {
            'upvotes': max(brain_feed.upvotes, 0),
            'downvotes': max(brain_feed.downvotes, 0)
        }
        brain_feed.save()

        return HttpResponse(json.dumps(votes), content_type='application/json')


