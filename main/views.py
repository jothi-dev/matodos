from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList

# Create your views here.
def home(request):
    return render(request, "main/home.html", {})

def create(request):
    if request.method == "POST":
        form = CreateNewList(request.POST)

        if form.is_valid():
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            # request.user.todolist.add(t)
    
        return HttpResponseRedirect("/todos")
        # return HttpResponseRedirect("/view/todo/%i" %t.id)
    else:
        form = CreateNewList()
        return render(request, "main/create.html", {"form":form})

def todos(request):
    todos = ToDoList.objects.all()
    return render(request, "main/todos.html", {"todos": todos})

def view_todo(request, id):
    todo = ToDoList.objects.get(id=id)
    return render(request, "main/view_todo.html", {"todo": todo})

def delete_todo(request, id):
    _todo = ToDoList.objects.filter(id=id).delete()

    return HttpResponseRedirect("/todos")

