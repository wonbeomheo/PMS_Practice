from django.contrib import admin

from .models import User, Task, Project
# Register your models here.

admin.site.register(User)
admin.site.register(Task)
admin.site.register(Project)