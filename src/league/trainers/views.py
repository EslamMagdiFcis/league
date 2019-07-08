from django.db.models import Q

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly

from .serializers import TrainerListSerializer, TrainerCreateSerializer
from players.pagination import PlayerLimitOffsetPagination
from .models import Trainer


class TrainerListAPIView(ListAPIView):
    serializer_class = TrainerListSerializer
    permission_classes = [AllowAny]
    pagination_class = PlayerLimitOffsetPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['first_name', 'last_name', 'title']

    def get_queryset(self):
        query_list = Trainer.objects.all()
        query = self.request.GET.get('q')
        if query:
            query_list = query_list.filter(Q(first_name__icontains=query) |
                                           Q(last_name__icontains=query) |
                                           Q(title__icontains=query))

        return query_list


class TrainerCreateAPIView(CreateAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerCreateSerializer
    permission_classes = [IsAuthenticated]


class TrainerDetailUpdateDeleteAPIView(UpdateModelMixin, DestroyModelMixin, RetrieveAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerCreateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)
