from django.urls import path

from .views import TeamCreateAPIView, TeamDetailUpdateDeleteAPIView, TeamListAPIView

app_name = 'teams-api'

urlpatterns = [
    path('', TeamListAPIView.as_view(), name='list'),
    path('create/', TeamCreateAPIView.as_view(), name='create'),
    path('<int:pk>/', TeamDetailUpdateDeleteAPIView.as_view(), name='detail'),
]
