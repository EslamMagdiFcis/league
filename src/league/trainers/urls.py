from django.urls import path

from .views import TrainerDetailAPIView, TrainerListCreateAPIView

app_name = 'trainers-api'

urlpatterns = [
    path('', TrainerListCreateAPIView.as_view(), name='list-create'),
    path('<int:pk>/', TrainerDetailAPIView.as_view(), name='detail'),
]
