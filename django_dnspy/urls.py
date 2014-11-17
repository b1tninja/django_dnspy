from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

from django.views.generic import ListView
from dnspy.models import Name, Record, Question, Query

urlpatterns = patterns('',
    (r'^names/$', ListView.as_view(model=Name,)),
    (r'^questions/$', ListView.as_view(model=Question,)),
    (r'^records/$', ListView.as_view(model=Record,)),
    (r'^queries/$', ListView.as_view(model=Query,)),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
