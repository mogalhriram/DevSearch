from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required  #decorator for authrization
from django.contrib import messages
from django.db.models import query
from django.shortcuts import redirect, render


from .utils import searchProfiles, paginateProfiles
from .models import Profile, Skill
from django.contrib.auth import authenticate, login, logout
from .forms import CustomUserCreationForm, ProfileForm, SkillForm


# Create your views here.



def registerUser(request):
    form = CustomUserCreationForm()
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid:
            user = form.save(commit=False)  #return instance before saving
            user.username = user.username.lower()
            user.save()
            messages.success(request, "User registered Succesfully !")
            login(request,user)
            return redirect("edit-account")
        else:
            messages.error(request, "Error occurred during registration !")
            return redirect("register")

    page = "register"
    context ={"page": page, "form":form}
    return render(request,"users/login-register.html", context)

def logoutUser(request):
    logout(request) #This will delet tha session from table
    messages.error(request,"User logged out")
    return redirect("login")

def loginUser(request):
    page = "login"
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
        # returns None if password not matched
        
        if user is not None:
            login(request, user) #It will create session for this user in database
                                    #check inspect --> application --> cookies
            return redirect (request.GET['next'] if 'next'  in request.GET else 'account')
        else:
            messages.error(request,"Invalid username or password")
    context={"page":page}
    return render(request,'users/login-register.html',context)


def profiles(request):
    profiles, search_query = searchProfiles(request)
    paginator, profiles, custom_range = paginateProfiles(request,profiles)
    context = {'profiles': profiles, "search_query": search_query, "query_set":profiles, "custom_range":custom_range, "paginator": paginator}
    return render(request,"users/profiles.html",context)


def profile(request,pk):
    profile = Profile.objects.get(id = pk)
    topSkill = profile.skill_set.exclude(description__exact="")
    otherSkill = profile.skill_set.filter(description="")
    context = {"profile":profile,"topSkill": topSkill,"otherSkill": otherSkill }
    return render(request,"users/user-profile.html",context)

@login_required(login_url="login")
def userAccount(request):
    profile = request.user.profile
    skills = profile.skill_set.all()
    projects = profile.project_set.all()
    context ={"profile": profile, "skills":skills,"projects":projects}
    return render(request,"users/account.html", context)


@login_required(login_url="login")
def editAccount(request):
    profile = request.user.profile
    form = ProfileForm(instance=profile)
    context = {"form": form}
    if request.method == "POST":
            form = ProfileForm(request.POST, request.FILES, instance=profile)
            if form.is_valid:
                form.save()
                return redirect("account")

    return render(request, "users/profile-form.html", context)

@login_required(login_url="login")
def addSkill(request):
    profile = request.user.profile
    form = SkillForm()
    context={"form": form}
    if request.method == "POST":
        form = SkillForm(request.POST)
        if form.is_valid:
            skill = form.save(commit=False)
            skill.owner=profile
            skill.save()
            messages.success(request,"Skill Added")
            return redirect("account")
    return render(request, "users/skill-form.html", context)

@login_required(login_url="login")
def updateSkill(request,pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    if request.method == "POST":
        form = SkillForm(request.POST, instance=skill)
        if form.is_valid:
            form.save()
            messages.success(request,"Skill Updated")
            return redirect("account")
    form = SkillForm(instance = skill)
    context ={"form": form}
    return render(request,"users/skill-form.html",context)

@login_required(login_url="login")
def deleteSkill(request, pk):
    profile = request.user.profile
    skill = profile.skill_set.get(id=pk)
    if request.method == "POST":
        skill.delete()
        messages.error(request,"Skill Deleted")
        return redirect("account")
    context ={"object":skill}
    return render(request, "delete_template.html",context)