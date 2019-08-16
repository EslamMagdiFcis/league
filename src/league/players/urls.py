from django.urls import path

from .views import PlayerCreateAPIView, PlayerDetailUpdateDeleteAPIView, PlayerListAPIView  # , PlayerUpdateAPIView

app_name = 'players-api'

urlpatterns = [
    path('', PlayerListAPIView.as_view(), name='list'),
    path('create/', PlayerCreateAPIView.as_view(), name='create'),
    path('<int:pk>/', PlayerDetailUpdateDeleteAPIView.as_view(), name='detail-delete'),
]
