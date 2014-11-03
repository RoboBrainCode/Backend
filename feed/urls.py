from django.conf.urls import patterns, url
from feed import views

urlpatterns = patterns('',
    url(r'most_recent/', views.return_top_k_feeds, name='most_recent'),
    url(r'infinite_scroll/', views.infinite_scrolling, name='infinite_scrolling'),
    url(r'filter/', views.filter_feeds_with_hashtags, name='filter'),
    url(r'filter_type/', views.filter_feeds_with_type, name='filter_type'),
    url(r'since/', views.return_feeds_since, name='since'),
    url(r'upvotes/', views.upvotes_recorder, name='upvotes'),
    url(r'graph_feedback/', views.save_graph_feedback, name='graph_feedback'),
)
