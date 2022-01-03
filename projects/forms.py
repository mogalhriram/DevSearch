
from django.db import models
from django.forms import ModelForm, fields
from django.forms.widgets import CheckboxSelectMultiple
from .models import Project, Review
from django import forms

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'featured_image','description','source_link', 'demo_link', 'tag']
        
        widgets = {
            'tag' : forms.CheckboxSelectMultiple(),
        }

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields= ['value', 'body']
    
        labels ={
            'value': 'Place Your Vote',
            'body': 'Add comment', 
        }
