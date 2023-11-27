from django.shortcuts import render
from django.views import generic

from todo_app.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task
    queryset = Task.objects.prefetch_related("tags").order_by('is_done', 'created_at')


class TagListView(generic.ListView):
    model = Tag

