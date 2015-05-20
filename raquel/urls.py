from django.conf.urls import patterns, url
from raquel import views
urlpatterns = patterns('',
    url(r'rachQuery/', views.rachQuery, name='rachQuery'),)
