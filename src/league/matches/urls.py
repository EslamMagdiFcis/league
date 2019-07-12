from django.urls import path

from .views import MatchCreateAPIView, MatchDetailDeleteAPIView, MatchListAPIView, MatchUpdateAPIView

app_name = 'matches-api'

urlpatterns = [
    path('', MatchListAPIView.as_view(), name='list'),
    path('create/', MatchCreateAPIView.as_view(), name='create'),
    path('<int:pk>/', MatchDetailDeleteAPIView.as_view(), name='detail-delete'),
    path('<int:pk>/edit', MatchUpdateAPIView.as_view(), name='update'),
]
