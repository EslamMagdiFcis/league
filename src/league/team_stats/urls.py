from django.urls import path

from .views import TeamStatsCreateAPIView, TeamStatsDetailDeleteAPIView, TeamStatsListAPIView, TeamStatsUpdateAPIView

app_name = 'team-stats-api'

urlpatterns = [
    path('', TeamStatsListAPIView.as_view(), name='list'),
    path('create/', TeamStatsCreateAPIView.as_view(), name='create'),
    path('<int:pk>/', TeamStatsDetailDeleteAPIView.as_view(), name='detail-delete'),
    path('<int:pk>/edit', TeamStatsUpdateAPIView.as_view(), name='update'),
]
