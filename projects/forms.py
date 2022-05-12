from django import forms


class ProjectForm(forms.Form):
    form_post = forms.CharField(widget = forms.TextInput)