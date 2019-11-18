from django.shortcuts import render
from django.views import generic
from . import models
from django.shortcuts import get_object_or_404

# Create your views here.


class PublisherList(generic.ListView):
    model = models.Publisher
    template_name = "publishers.html"
    context_object_name = "publishers"
    queryset = models.Publisher.objects.all()


class PublisherDetail(generic.DetailView):

    model = models.Publisher
    template_name = "publisher_detail.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(PublisherDetail, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['book_list'] = models.Book.objects.filter(publisher__pk=self.kwargs['pk'])
        return context
