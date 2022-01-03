from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    username = models.CharField(max_length=200, blank=True, null=True)
    email = models.EmailField(max_length=500, blank=True, null=True)
    short_intro = models.CharField(max_length=500, blank=True,null=True)
    intro = models.TextField(max_length=500, blank=True,null=True)
    profile_image = models.ImageField(
        null = True, blank= True, upload_to = 'profiles/',default='profiles/user-default.png')
    location = models.CharField(max_length=200, blank=True, null=True)
    social_github = models.CharField(max_length=200, blank=True, null=True)
    social_twitter = models.CharField(max_length=200, blank=True, null=True)
    social_linkedin = models.CharField(max_length=200, blank=True, null=True)
    social_website = models.CharField(max_length=200, blank=True, null=True)
    social_stackoverflow = models.CharField(max_length=200, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                                     primary_key=True, editable=False)

                                     
    def __str__(self) -> str:
        return str(self.user.username)
    
    class Meta:
        ordering = ["created"]


class Skill(models.Model):
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description =  models.TextField(max_length=500, blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                                     primary_key=True, editable=False)
    def __str__(self) -> str:
        return str(self.name)


class Message(models.Model):
    sender = models.ForeignKey(Profile , on_delete=models.SET_NULL , null=True, blank=True)
    recipient = models.ForeignKey(Profile, on_delete=models.SET_NULL, blank=True, null=True, related_name="messages") #it should be table_column_fk
    name = models.CharField(max_length=200, null=True, blank=True)  #sender_name
    email = models.CharField(max_length=200, null=True, blank=True) # follow
    subject = models.CharField(max_length=200, null=True, blank=True)
    body = models.TextField()
    is_read = models.BooleanField(default=False, null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                                     primary_key=True, editable=False)
    
    def __str__(self) -> str:
        return self.subject
    
    class Meta:
        ordering = ["is_read", "-created"]
