from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

from django.views.generic import ListView, TemplateView
from dnspy.models import Name, Record, Question, Query

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^names/$', ListView.as_view(model=Name,), name='name_list'),
    url(r'^questions/$', ListView.as_view(model=Question,), name='question_list'),
    url(r'^records/$', ListView.as_view(model=Record,), name='record_list'),
    url(r'^queries/$', ListView.as_view(model=Query,), name='query_list'),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
