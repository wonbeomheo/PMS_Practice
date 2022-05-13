from django import forms
from .models import User

# iterables
USER_CHOICES = []
for user in User.objects.all():
    USER_CHOICES.append((user.id, user.name))

TEAM_CHOICES = [
        (0, 'CEO'),
        (1, 'Development'),
        (2, 'Design'),
        (3, 'Data'),
    ]


class ProjectForm(forms.Form):
    project_title = forms.CharField(label='Project Title', max_length=200)
    user_id = forms.ChoiceField(label='User', choices=USER_CHOICES)
    start_date = forms.DateField(label='Start date')
    end_date = forms.DateField(label='End date')


class UserForm(forms.Form):
    user_team = forms.ChoiceField(label='team', choices=TEAM_CHOICES)
    user_name = forms.CharField(label='User Name', max_length=200)
    user_password = forms.CharField(label='Password', max_length=12, widget=forms.PasswordInput)