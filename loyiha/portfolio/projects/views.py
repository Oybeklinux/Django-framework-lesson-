from django.http import HttpRequest, JsonResponse
from django.shortcuts import render

# Create your views here.

def projects(request):
    return HttpRequest("Loyihalar")