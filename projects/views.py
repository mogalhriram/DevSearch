from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.core.paginator import Paginator
from .utils import searchProjects
from .models import Project
from .forms import ProjectForm

# Create your views here.
def projects(request):
    projects, search_query =searchProjects(request)
    context = {"projects": projects, "search_query": search_query}
    return render(request,"projects/projects.html",context)

def project(request,pk):
    project_obj = Project.objects.get(id=pk)
    tags = project_obj.tag.all()
    return render(request, "projects/project.html",{'project': project_obj, "tags": tags})

@login_required(login_url="login")
def creatProject(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == 'POST':
       form = ProjectForm(request.POST, request.FILES)
       if form.is_valid:
             project = form.save(commit=False)
             project.owner=profile
             project.save()
             return redirect('account')
    context = {'form': form}
    return render(request,'projects/project_form.html', context)

@login_required(login_url="login")
def updateProject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST':
       form = ProjectForm(request.POST, request.FILES, instance=project)
       if form.is_valid:
             form.save()
             return redirect('account')
    context = {'form': form}
    return render(request,'projects/project_form.html', context)

@login_required(login_url="login")
def deleteProject(request,pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)   #this is for delete project related to this project
    if request.method=='POST':
        project.delete()
        return redirect('account')
    context = {'object':project}
    return render(request, 'delete_template.html',context)

