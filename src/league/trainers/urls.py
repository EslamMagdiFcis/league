from django.urls import path

from .views import TrainerCreateAPIView, TrainerDetailUpdateDeleteAPIView, TrainerListAPIView

app_name = 'trainers-api'

urlpatterns = [
    path('', TrainerListAPIView.as_view(), name='list'),
    path('create/', TrainerCreateAPIView.as_view(), name='create'),
    path('<int:pk>/', TrainerDetailUpdateDeleteAPIView.as_view(), name='detail'),
]
