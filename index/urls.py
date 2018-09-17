from django.conf.urls import url

from index.views import *

urlpatterns = [
    url(r'^login/$',login_views),
    url(r'^check_login/$',check_login_views),
    url(r'^get_info/$',get_info_views),
    url(r'^$',index_views),
]