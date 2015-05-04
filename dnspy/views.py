from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView
from dnspy.models import Name, ResourceHeader, ResourceRecord, Packet, PacketQuestion, PacketRecord, Query

class NameDetailView(DetailView):
    context_object_name = "name"
    model = Name

class ResourceHeaderDetailView(DetailView):
    context_object_name = "resource_header"
    model = ResourceHeader

class QueryDetailView(DetailView):
    context_object_name = "query"
    model = Query

class ResourceRecordDetailView(DetailView):
    context_object_name = "resource_record"
    model = ResourceRecord




    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super(NameDetailView, self).get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     context['book_list'] = Book.objects.all()
    #     return context