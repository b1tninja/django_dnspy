from django.shortcuts import render

# Create your views here.
from django.views.generic import DetailView
from dnspy.models import Name, Question, Query, Record

class NameDetailView(DetailView):
    context_object_name = "name"
    model = Name

class QuestionDetailView(DetailView):
    context_object_name = "question"
    model = Question

class QueryDetailView(DetailView):
    context_object_name = "query"
    model = Query

class RecordDetailView(DetailView):
    context_object_name = "record"
    model = Record




    # def get_context_data(self, **kwargs):
    #     # Call the base implementation first to get a context
    #     context = super(NameDetailView, self).get_context_data(**kwargs)
    #     # Add in a QuerySet of all the books
    #     context['book_list'] = Book.objects.all()
    #     return context