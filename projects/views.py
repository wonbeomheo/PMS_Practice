from .models import User, Project, Task
from .forms import ProjectForm, UserForm

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, reverse


# Shows Project List
def index(request):
    prj_list = Project.objects.order_by('id')
    context = {'project_list': prj_list}
    return render(request, 'projects/index.html', context)


# Project Registration page
def reg_prj(request):
    user_list = User.objects.order_by('id')
    project_form = ProjectForm()
    context = {'user_list': user_list, 'project_form': project_form}
    return render(request, 'projects/prj_register.html', context)


# Post a new project
def get_project(request):
    if request.method == 'POST':
        project_form = ProjectForm(request.POST)
        if project_form.is_valid():
            submitted_project = Project(title=project_form.cleaned_data['project_title'],
                                        user_id=project_form.cleaned_data['user_id'],
                                        start_date=project_form.cleaned_data['start_date'],
                                        deadline_date=project_form.cleaned_data['end_date']
                                        )
            submitted_project.save()
            return HttpResponseRedirect(reverse('projects:project', args=(Project.objects.count(), )))
    else:
        project_form = ProjectForm()
    return render(request, 'projects/prj_register.html', {'project_form': project_form})


# User Registration page
def reg_usr(request):
    user_form = UserForm()
    return render(request, 'projects/usr_register.html', {'user_form': user_form})


# Post a new user
def get_user(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            submitted_user = User(name=user_form.cleaned_data['user_name'],
                                  team=user_form.cleaned_data['user_team'],
                                  )
            submitted_user.save()
            return HttpResponseRedirect(reverse('projects:user', args=(User.objects.count(),)))
    else:
        user_form = UserForm()
    return render(request, 'projects/usr_register.html', {'user_form': user_form})


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
