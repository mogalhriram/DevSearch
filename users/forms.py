from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db.models import fields
from django.forms.models import ModelForm
from .models import Profile, Skill, Message




class  CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name", "email", "username", "password1", "password2"]
        labels={
            "first_name": "Name",
        }


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['name', 'username', 'email', 'short_intro', 'intro', 'profile_image',
        'location', 'social_github', 'social_twitter', 'social_linkedin',
        'social_website', 'social_stackoverflow',
        ]

class SkillForm(ModelForm):
    class Meta:
        model = Skill
        fields = ['name', 'description']

class MessageForm(ModelForm):
    class Meta:
        model = Message
        fields = ['name', 'email', 'subject', 'body']