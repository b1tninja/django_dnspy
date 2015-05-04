from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings

from django.views.generic import ListView, TemplateView

from dnspy.models import Name, ResourceHeader, ResourceRecord, Packet, PacketQuestion, PacketRecord, Blacklist, Query
from dnspy.views import NameDetailView, ResourceHeaderDetailView, ResourceRecordDetailView, QueryDetailView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url(r'^names/$', ListView.as_view(model=Name,), name='name_list'),
    url(r'^name/(?P<pk>\d+)/$', NameDetailView.as_view(), name='name'),
    url(r'^resource_headers/$', ListView.as_view(model=ResourceHeader,), name='resource_header_list'),
    url(r'^resource_header/(?P<pk>\d+)/$', ResourceHeaderDetailView.as_view(), name='resource_header'),
    url(r'^resource_records/$', ListView.as_view(model=ResourceRecord,), name='resource_record_list'),
    url(r'^resource_record/(?P<pk>\d+)/$', ResourceRecordDetailView.as_view(), name='resource_record'),
    url(r'^queries/$', ListView.as_view(model=Query,), name='query_list'),
    url(r'^query/(?P<pk>\d+)/$', QueryDetailView.as_view(), name='query'),
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
