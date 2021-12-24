from django.db import models
from django.forms import ModelForm, fields
from .models import Project

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_image','decription', 'demo_link', 'sorce_link', 'tag']
