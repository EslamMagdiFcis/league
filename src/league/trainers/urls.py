from django.urls import path

from .views import TrainerCreateAPIView, TrainerDetailAPIView, TrainerListAPIView, TrainerUpdateDeleteAPIView

app_name = 'trainers-api'

urlpatterns = [
    path('', TrainerListAPIView.as_view(), name='list'),
    path('create/', TrainerCreateAPIView.as_view(), name='create'),
    path('<int:pk>/', TrainerDetailAPIView.as_view(), name='detail'),
    path('<int:pk>/edit/', TrainerUpdateDeleteAPIView.as_view(), name='update-delete'),
]
