from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
    url(r'^$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    #url(r'^register/$', register),

    url(r'^home/$', home),
    url(r'^createuser/$', create_user),
    url(r'^createproject/$', create_project),
    url(r'^createclient/$', create_client),
    url(r'^createcourse/$', create_course),
    url(r'^p_ajax/$', p_ajax),
    url(r'^user_statustimesheet/$', user_statustimesheet)



)
