from django.urls import path

from .views import PlayerCreateAPIView, PlayerDetailAPIView, PlayerListAPIView, PlayerUpdateDeleteAPIView

app_name = 'players-api'

urlpatterns = [
    path('', PlayerListAPIView.as_view(), name='list'),
    path('create/', PlayerCreateAPIView.as_view(), name='create'),
    path('<int:pk>/', PlayerDetailAPIView.as_view(), name='detail'),
    path('<int:pk>/edit', PlayerUpdateDeleteAPIView.as_view(), name='update-delete'),
]
