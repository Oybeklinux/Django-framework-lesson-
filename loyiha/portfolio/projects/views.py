from django.http import HttpResponse
from django.shortcuts import render
from .models import *
# Create your views here.


def projects(request):
    items = Project.objects.all().values()
    return render(request, "projects/projects.html")


def project(request, pk):
    item = Project.objects.get(id=pk)
    return HttpResponse(item.__dict__.items())
