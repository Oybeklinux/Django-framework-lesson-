from django.http import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.
from .forms import ProjectForm

def projects(request):
    items = Project.objects.all()
    return render(request, "projects/projects.html", {"items": items})


def project(request, pk):
    item = Project.objects.get(id=pk)
    return render(request, "projects/project.html", {"item": item})


def add_project(request):
    form = ProjectForm()
    return render(request, "projects/add_project.html", {"form": form})
