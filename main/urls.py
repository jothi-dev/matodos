from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home, name="home"),
    path("todos/", views.todos, name="todos"),
    # path("<int:id>", views.list, name='list'),
    path("create/todo", views.create, name="create"),
    path("view/todo/<int:id>", views.view_todo, name="view_todo"),
    path("delete/todo/<int:id>", views.delete_todo, name="delete_todo")
]