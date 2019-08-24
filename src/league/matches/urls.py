from django.urls import path

from .views import MatchCreateAPIView, MatchRetrieveUpdateDestroyAPIView, MatchListAPIView

app_name = 'matches-api'

urlpatterns = [
    path('', MatchListAPIView.as_view(), name='list'),
    path('create/', MatchCreateAPIView.as_view(), name='create'),
    path('<int:pk>/', MatchRetrieveUpdateDestroyAPIView.as_view(), name='detail-delete'),
]
