from django import forms


class ProjectForm(forms.Form):
    project_title = forms.CharField(label='Project Title', max_length=200)
    user_id = forms.IntegerField(label='User')
    start_date = forms.DateField(label='Start date')
    end_date = forms.DateField(label='End date')


class UserForm(forms.Form):
    user_name = forms.CharField(label='User Name', max_length=200)
    user_team = forms.IntegerField(label='Team')