
from django.db import models
from django.forms import ModelForm, fields
from django.forms.widgets import CheckboxSelectMultiple
from .models import Project
from django import forms

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_image','decription','source_link', 'demo_link', 'tag']
        
        widgets = {
            'tag' : forms.CheckboxSelectMultiple(),
        }
