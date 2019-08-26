from django.urls import path

from .views import TeamStatsRetrieveUpdateDestroyAPIView, TeamStatsListCreateAPIView

app_name = 'team-stats-api'

urlpatterns = [
    path('', TeamStatsListCreateAPIView.as_view(), name='list-create'),
    path('<int:pk>/', TeamStatsRetrieveUpdateDestroyAPIView.as_view(), name='detail-delete-update'),
]
