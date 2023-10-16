from django import forms
from .models import project

class addProjectForm(forms.ModelForm):
    class Meta:
        model=project
        fields='__all__'
        widgets={
            'tag':forms.CheckboxSelectMultiple
        }

