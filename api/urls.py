from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('',views.getRoutes,name='get-routes'),
    path('projects/',views.getProjects,name='get-projects'),
    path('projects/project/<str:pk>/',views.project,name='get-project'),
    path('projects/project/',views.project,name='post-project'),

    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]