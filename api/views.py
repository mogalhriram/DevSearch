from django.http import JsonResponse
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .serializer import ProjectSearilizer
from projects.models import Project

@api_view((['GET']))
def getRoutes(request):

    routes = [
        {'GET': 'api/projects'},
        {'GET': 'api/projects/id'},
        {'POST': 'api/projects/id/vote'},

        {'POST': 'api/users/token'},
        {'POST': 'api/users/token/refresh'},
    ]


    return Response(routes)  

@api_view(['GET'])
#@permission_classes([IsAuthenticated])
def getProjects(request):
    projects = Project.objects.all()
    searializer = ProjectSearilizer(projects, many=True)
    return Response(searializer.data)


@api_view(['GET'])
def getProject(request,pk):
    projects = Project.objects.get(id=pk)
    searializer = ProjectSearilizer(projects, many=False)
    return Response(searializer.data)
