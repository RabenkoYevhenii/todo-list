from django.shortcuts import render
from django.views import generic

from todo_app.models import Task


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags")

    def get_queryset(self):
        return Task.objects.order_by('is_done', 'created_at')

