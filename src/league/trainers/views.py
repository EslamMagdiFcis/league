from django.db.models import Q

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly

from .serializers import TrainerSerializer
from players.pagination import PlayerLimitOffsetPagination
from .models import Trainer


class TrainerListCreateAPIView(ListCreateAPIView):
    serializer_class = TrainerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
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


class TrainerDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
