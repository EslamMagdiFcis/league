from django.urls import path

from .views import PlayerDetailUpdateDeleteAPIView, PlayerListCreateAPIView

app_name = 'players-api'

urlpatterns = [
    path('', PlayerListCreateAPIView.as_view(), name='list-create'),
    path('<int:pk>/', PlayerDetailUpdateDeleteAPIView.as_view(), name='detail-delete-update'),
]
