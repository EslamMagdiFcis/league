from django.urls import path

from .views import TeamStatsCreateAPIView, TeamStatsRetrieveUpdateDestroyAPIView, TeamStatsListAPIView

app_name = 'team-stats-api'

urlpatterns = [
    path('', TeamStatsListAPIView.as_view(), name='list'),
    path('create/', TeamStatsCreateAPIView.as_view(), name='create'),
    path('<int:pk>/', TeamStatsRetrieveUpdateDestroyAPIView.as_view(), name='detail-delete-update'),
]
