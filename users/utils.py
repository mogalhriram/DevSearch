from .models import Skill, Profile
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def searchProfiles(request):
    search_query = ""
    if request.GET.get("search_query"):
        search_query = request.GET.get("search_query")  
    skills = Skill.objects.filter(name__icontains =search_query)
    profiles = Profile.objects.distinct().filter(Q(name__icontains=search_query) | 
    Q(short_intro__icontains=search_query) |
    Q(skill__in=skills))
    return profiles, search_query

def paginateProfiles(request,profiles):
    page = request.GET.get('page')
    results = 9
    paginator = Paginator(profiles,results)
    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page=1
        profiles= paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profiles=paginator.page(page)

    left_index = int(page)-1
    if left_index<1:
        left_index=1

    right_index = int(page)+1
    if right_index> paginator.num_pages:
        right_index = paginator.num_pages

    custom_range =range(left_index, right_index+1)

    return paginator, profiles, custom_range
