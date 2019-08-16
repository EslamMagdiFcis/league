"""league URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/players/', include('players.urls', namespace='players-api')),
    path('api/trainers/', include('trainers.urls', namespace='trainers-api')),
    path('api/teams/', include('teams.urls', namespace='teams-api')),
    path('api/team-stats/', include('team_stats.urls', namespace='team-stats-api')),
    path('api/match/', include('matches.urls', namespace='matches-api')),
    path('api/user/', include('users.urls', namespace='users-api')),

    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='obtain-jwt-token'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='refresh-jwt-token'),
]
