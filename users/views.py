from django.shortcuts import render
from .models import Profile

# Create your views here.

def profiles(request):
    profiles = Profile.objects.all()
    return render(request,"users/profiles.html",{'profiles': profiles})

def profile(request,pk):
    profile = Profile.objects.get(id = pk)
    topSkill = profile.skill_set.exclude(description__exact="")
    otherSkill = profile.skill_set.filter(description="")
    context = {"profile":profile,"topSkill": topSkill,"otherSkill": otherSkill }
    return render(request,"users/user-profile.html",context)
