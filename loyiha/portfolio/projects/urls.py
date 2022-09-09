from django.urls import path, include
from .views import *

urlpatterns = [
    path('projects/', projects),
    path('projects/<int:pk>', project, name='project'),
    path('add_project/', add_project, name="add_project"),

]
