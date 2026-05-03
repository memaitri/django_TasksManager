from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms

class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority (1=Low, 10=High)", min_value=1, max_value=10)

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []

    # Ensure all tasks are dicts (for backward compatibility)
    tasks = request.session["tasks"]
    for i, t in enumerate(tasks):
        if isinstance(t, str):
            tasks[i] = {"task": t, "priority": 1, "done": False}
        elif isinstance(t, dict):
            if "done" not in t:
                t["done"] = False
            if "priority" not in t:
                t["priority"] = 1
            if "task" not in t:
                t["task"] = str(t)
    request.session["tasks"] = tasks

    # Sort tasks by priority (highest first)
    sorted_tasks = sorted(
        enumerate(request.session["tasks"]),  # keep original index
        key=lambda x: x[1]["priority"],
        reverse=True
    )

    return render(request, "tasks/index.html", {
        "tasks": sorted_tasks  # list of (original_index, task_dict)
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            if "tasks" not in request.session:
                request.session["tasks"] = []

            task = form.cleaned_data["task"]
            priority = form.cleaned_data["priority"]
            request.session["tasks"] += [{"task": task, "priority": priority, "done": False}]
            return HttpResponseRedirect(reverse("tasks:index"))
        else:
            return render(request, "tasks/add.html", {"form": form})

    return render(request, "tasks/add.html", {"form": NewTaskForm()})

def delete(request, index):
    if "tasks" in request.session:
        tasks = request.session["tasks"]
        if 0 <= index < len(tasks):
            tasks.pop(index)
            request.session["tasks"] = tasks  # reassign to trigger session save
    return HttpResponseRedirect(reverse("tasks:index"))

def toggle(request, index):
    if "tasks" in request.session:
        tasks = request.session["tasks"]
        if 0 <= index < len(tasks):
            if not isinstance(tasks[index], dict):
                tasks[index] = {"task": str(tasks[index]), "priority": 1, "done": False}
            if "done" not in tasks[index]:
                tasks[index]["done"] = False
            tasks[index]["done"] = not tasks[index]["done"]
            request.session["tasks"] = tasks  # reassign to trigger session save
    return HttpResponseRedirect(reverse("tasks:index"))