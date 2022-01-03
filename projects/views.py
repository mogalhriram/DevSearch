from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.contrib import messages
from .utils import searchProjects, paginateProjects
from .models import Project
from .forms import ProjectForm, ReviewForm

# Create your views here.



def projects(request):
    projects, search_query =searchProjects(request)
    paginator, projects, custom_range = paginateProjects(request,projects)
    context = {"projects": projects, "search_query": search_query, "paginator": paginator, "custom_range": custom_range, "query_set": projects}
    return render(request,"projects/projects.html",context)

def project(request,pk):
    form = ReviewForm()
    project_obj = Project.objects.get(id=pk)

    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.project = project_obj
            review.owner = request.user.profile
            review.save()
            project_obj.getVoteCount
            messages.success(request, "Review Added")
            return redirect('project', project_obj.id)
        else:
            messages.error(request, "Error occurred !")
       

    tags = project_obj.tag.all()
    context = {'project': project_obj, "tags": tags, "form": form}
    return render(request, "projects/project.html", context)

@login_required(login_url="login")
def creatProject(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method == 'POST':
       form = ProjectForm(request.POST, request.FILES)
       if form.is_valid():
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
       if form.is_valid():
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

