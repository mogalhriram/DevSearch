from .models import Project, Tag
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def searchProjects(request):
    search_query = ""
    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query")
    tags = Tag.objects.filter(name__icontains = search_query)
    projects = Project.objects.distinct().filter(
        Q(title__icontains = search_query) |
        Q(tag__in = tags)
        )
    return projects, search_query

def paginateProjects(request,projects):
    page = request.GET.get('page')
    results = 9
    paginator = Paginator(projects,results)
    try:
        if page == None:
            page=1
        projects = paginator.page(page)
    except PageNotAnInteger:
        page=1
        projects= paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        projects=paginator.page(page)


    left_index = int(page)-1
    if left_index<1:
        left_index=1

    right_index = int(page)+1
    if right_index> paginator.num_pages:
        right_index = paginator.num_pages

    custom_range =range(left_index, right_index+1)

    return paginator, projects, custom_range