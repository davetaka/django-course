import json

from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (TemplateView, View, ListView, DetailView)
from django.contrib import messages
from django.http import HttpResponse

from .models import Thread, Reply


# sample of normal View
# class ForumView(View):

#     # template_name = 'forum/index.html'
#     def get(self, request, *args, **kwargs):
#         return render(request, 'forum/index.html')

# sample of template view
# class ForumView(TemplateView):

#     template_name = 'forum/index.html'
# index = ForumView.as_view()
# or
# index = ForumView.as_view(template_name="forum/index.html")

class ForumView(ListView):

    paginate_by = 2
    template_name = 'forum/index.html'

    def get_queryset(self):
        queryset = Thread.objects.all()
        order = self.request.GET.get('order', '')
        if order == 'views':
            queryset = queryset.order_by('-views')
        elif order == 'answers':
            queryset = queryset.order_by('-answers')
        tag = self.kwargs.get('tag', '')
        if tag:
            queryset = queryset.filter(tags__slug__icontains=tag)
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ForumView, self).get_context_data(**kwargs)
        context['tags'] = Thread.tags.all()
        return context


index = ForumView.as_view()
