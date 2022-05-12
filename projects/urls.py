from django.urls import path


from . import views

app_name = 'projects'
urlpatterns = [
    # Project List page
    path('', views.index, name='index'),
    # Project page
    path('<int:project_id>/', views.project, name='project'),
    # Task page
    path('<int:project_id>/<int:task_id>/', views.task, name='task'),
    # User List page
    path('users/', views.users, name='users'),
    # User page
    path('users/<int:user_id>/', views.user, name='user'),
    # Project Registration page
    path('reg/', views.reg_prj, name='prj_registration'),
]