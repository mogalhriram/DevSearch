from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .utils import searchProjects, paginateProjects
from .models import Project
from .forms import ProjectForm

# Create your views here.


def projects(request):
    projects, search_query =searchProjects(request)
    paginator, projects, custom_range = paginateProjects(request,projects)
    context = {"projects": projects, "search_query": search_query, "paginator": paginator, "custom_range": custom_range, "query_set": projects}
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

