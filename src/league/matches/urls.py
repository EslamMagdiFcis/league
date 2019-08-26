from django.urls import path

from .views import MatchRetrieveUpdateDestroyAPIView, MatchListCreateAPIView

app_name = 'matches-api'

urlpatterns = [
    path('', MatchListCreateAPIView.as_view(), name='list-create'),
    path('<int:pk>/', MatchRetrieveUpdateDestroyAPIView.as_view(), name='detail-delete'),
]
