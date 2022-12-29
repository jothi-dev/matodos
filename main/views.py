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
            request.user.todolist.add(t)
    
        return HttpResponseRedirect("/%i" %t.id)

    else:
        form = CreateNewList()

        return render(request, "main/create.html", {"form":form})

def view_todo(request, id):
    todo = ToDoList.objects.get(id=id)
    return render(request, "main/view_todo.html", {"todo": todo})

def list(request, id):
    ls = ToDoList.objects.get(id=id)

    # if response.method == "POST":
    #     print(response.POST)
    #     if response.POST.get("save"):

    #         for item in ls.item_set.all():
    #             if response.POST.get("c" + str(item.id)) == "clicked":
    #                 item.complete = True
    #             else:
    #                 item.complete = False

    #             item.save()

    #     elif request.POST.get("newItem"):
    #         txt = response.POST.get("new")

    #         if len(txt) > 2:
    #             ls.item_set.create(text=txt, complete=False)
    #         else:
    #             print("invalid")


    return render(request, "main/list.html", {"ls": ls})


def todos(request):
    todos = ToDoList.objects.all()
    return render(request, "main/todos.html", {"todos": todos})
