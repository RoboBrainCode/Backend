from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Backend.views.home', name='home'),
    url(r'^feed/', include('feed.urls')),
    url(r'^auth/', include('auth.urls')),
    url(r'^api/',include('rest_api.urls')),
    url(r'^graph/',include('graph.urls')),
    url(r'^raquel/',include('raquel.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
