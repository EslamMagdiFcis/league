from django.urls import path

from .views import TeamDetailUpdateDeleteAPIView, TeamListCreateAPIView

app_name = 'teams-api'

urlpatterns = [
    path('', TeamListCreateAPIView.as_view(), name='list-create'),
    path('<int:pk>/', TeamDetailUpdateDeleteAPIView.as_view(), name='detail'),
]
