from django.urls import path
from .views import CreateUserAPIView, UserLoginAPIView

app_name = 'users-api'

urlpatterns = [
    path('register/', CreateUserAPIView.as_view()),
    path('login/', UserLoginAPIView.as_view())
]
