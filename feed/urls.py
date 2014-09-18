from django.conf.urls import patterns, url

from feed import views

urlpatterns = patterns('',
	url(r'most_recent\.(?P<extension>(json)|(js)|(xml))/', views.return_top_k_feeds, name='most_recent'),
	url(r'infinite_scroll\.(?P<extension>(json)|(js)|(xml))/', views.infinite_scrolling, name='infinite_scrolling'),
	url(r'filter\.(?P<extension>(json)|(js)|(xml))/', views.filter_feeds_with_hashtags, name='filter'),
	url(r'filter_type\.(?P<extension>(json)|(js)|(xml))/', views.filter_feeds_with_type, name='filter_type'),
	url(r'since\.(?P<extension>(json)|(js)|(xml))/', views.return_feeds_since, name='since'),
	url(r'upvotes\.(?P<extension>(json)|(js)|(xml))/', views.upvotes_recorder, name='upvotes'),
)
