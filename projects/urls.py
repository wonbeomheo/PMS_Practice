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
    # Project Registration Progress page
    path('reg/project_registration_progress/', views.get_project, name='prj_registration_progress'),
    # User Registration page
    path('urs_reg/', views.reg_usr, name='usr_registration'),
    # User Registration Progress page
    path('urs_reg/user_registration_progress/', views.get_user, name='usr_registration_progress'),
]