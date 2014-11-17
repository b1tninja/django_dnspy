from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

from django.views.generic import ListView, TemplateView

from dnspy.models import Name, Record, Question, Query
from dnspy.views import NameDetailView, QuestionDetailView, QueryDetailView, RecordDetailView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^names/$', ListView.as_view(model=Name,), name='name_list'),
    url(r'^name/(?P<pk>\d+)/$', NameDetailView.as_view(), name='name'),
    url(r'^questions/$', ListView.as_view(model=Question,), name='question_list'),
    url(r'^question/(?P<pk>\d+)/$', QuestionDetailView.as_view(), name='question'),
    url(r'^records/$', ListView.as_view(model=Record,), name='record_list'),
    url(r'^record/(?P<pk>\d+)/$', RecordDetailView.as_view(), name='record'),
    url(r'^queries/$', ListView.as_view(model=Query,), name='query_list'),
    url(r'^query/(?P<pk>\d+)/$', QueryDetailView.as_view(), name='query'),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
