from django.conf.urls import patterns, url
import auth

urlpatterns = patterns('',
    url(r'create_user/', auth.create_user_rb, name='create_user'),
    url(r'login/', auth.login_rb, name='login'),
    url(r'logout/', auth.logout_rb, name='logout')
)
