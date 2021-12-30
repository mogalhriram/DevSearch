from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required  #decorator for authrization

from django.contrib import messages

from django.shortcuts import redirect, render
from .models import Profile

from django.contrib.auth import authenticate, login, logout

# Create your views here.

def logoutUser(request):
    logout(request) #This will delet tha session from table
    messages.error(request,"User logged out")
    return redirect("login")

def loginUser(request):
    if request.user.is_authenticated:
        return redirect("profiles")
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request,"User not exists")
        
        user = authenticate(request, username = username, password = password) 
        # retruns None if password not matched
        
        if user is not None:
            login(request, user) #It will create session for this user in database
            #check inspect --> application --> cookies
            return redirect ("profiles")
        else:
            messages.error(request,"Invalid username or password")
    return render(request,'users/login-register.html')

def profiles(request):
    profiles = Profile.objects.all()
    return render(request,"users/profiles.html",{'profiles': profiles})

def profile(request,pk):
    profile = Profile.objects.get(id = pk)
    topSkill = profile.skill_set.exclude(description__exact="")
    otherSkill = profile.skill_set.filter(description="")
    context = {"profile":profile,"topSkill": topSkill,"otherSkill": otherSkill }
    return render(request,"users/user-profile.html",context)
