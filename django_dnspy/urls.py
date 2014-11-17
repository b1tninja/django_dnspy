from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.views.generic import ListView
from dnspy.models import Name, Record, Question, Query

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_dnspy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    (r'^names/$', ListView.as_view(model=Name,)),
#    (r'^questions/$', ListView.as_view(model=Question,)),
#    (r'^records/$', ListView.as_view(model=Record,)),
#    (r'^queries/$', ListView.as_view(model=Query,)),
    url(r'^admin/', include(admin.site.urls)),
)
