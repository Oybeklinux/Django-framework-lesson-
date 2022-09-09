from django.urls import path, include
from .views import *

urlpatterns = [
    path('projects/', projects),
    path('projects/<int:pk>', project)
]
