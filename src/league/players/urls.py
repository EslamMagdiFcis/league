from django.urls import path

from .views import PlayerCreateAPIView, PlayerDetailDeleteAPIView, PlayerListAPIView, PlayerUpdateAPIView

app_name = 'players-api'

urlpatterns = [
    path('', PlayerListAPIView.as_view(), name='list'),
    path('create/', PlayerCreateAPIView.as_view(), name='create'),
    path('<int:pk>/', PlayerDetailDeleteAPIView.as_view(), name='detail-delete'),
    path('<int:pk>/edit', PlayerUpdateAPIView.as_view(), name='update'),
]
