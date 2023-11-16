from todo.views import TodoListCreate, TodoDeleteShowUpdate

from django.urls import path

urlpatterns = [
    # /api/todo
    path("todo", TodoListCreate.as_view()),
    # /api/todo/5 - Fazer ação especifica em uma tarefa
    path("todo/<int:pk>", TodoDeleteShowUpdate.as_view()),
]
