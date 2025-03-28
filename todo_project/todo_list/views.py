from django.http import (
    HttpResponse, HttpRequest
)
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from .models import ToDoItem

def index_view(request: HttpRequest) -> HttpResponse:
    todo_items = ToDoItem.objects.all()[:3]
    return render(
        request,
        template_name="todo_list/index.html",
        context={"todo_items": todo_items}
    )


class ToDoListIndexView(ListView):
    template_name = "todo_list/index.html"
    queryset = ToDoItem.objects.all()[:2]

class ToDoListView(ListView):
    model = ToDoItem

class ToDoListDoneView(ListView):
    queryset = ToDoItem.objects.filter(done=True).all()[:2]


class ToDoDetailView(DetailView):
    model = ToDoItem

