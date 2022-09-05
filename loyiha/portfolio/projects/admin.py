from django.contrib import admin
from .models import *

admin.site.register(Project)
admin.site.register(Message)
admin.site.register(Tag)
admin.site.register(Review)
admin.site.register(Skill)

# Register your models here.
