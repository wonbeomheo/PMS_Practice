from .models import User, Project, Task
from .forms import ProjectForm
from django.shortcuts import render, get_object_or_404



# Shows Project List
def index(request):
    prj_list = Project.objects.order_by('id')
    context = {'project_list': prj_list}
    return render(request, 'projects/index.html', context)


def reg_prj(request):
    user_list = User.objects.order_by('id')
    context = {'user_list': user_list}
    return render(request, 'projects/prj_register.html', context)


def get_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        return render(request, 'projects/project.html', )


# Project Page
def project(request, project_id):
    selected_project = get_object_or_404(Project, pk=project_id)
    task_list = Task.objects.filter(
        project_id=project_id
    ).order_by('id')
    return render(request, 'projects/project.html', {'project': selected_project, 'task_list': task_list})


# Task Page
def task(request, project_id, task_id):
    selected_task = get_object_or_404(Task, pk=task_id)
    return render(request, 'projects/task.html', {'task': selected_task})


# User list page
def users(request):
    usr_list = User.objects.order_by('id')
    context = {'user_list': usr_list}
    return render(request, 'projects/users.html', context)


# User page
def user(request, user_id):
    selected_user = get_object_or_404(User, pk=user_id)
    return render(request, 'projects/user.html', {'user': selected_user})