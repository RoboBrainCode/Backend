from django.conf.urls import patterns, url
from graph import views

urlpatterns = patterns('',
    url(r'getNode/', views.getNode, name='getNode'),
    
)
