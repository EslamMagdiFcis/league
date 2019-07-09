from django.db.models import Q

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly

from .serializers import PlayerListSerializer, PlayerCreateSerializer, PlayerUpdateDeleteSerializer
from .pagination import PlayerLimitOffsetPagination
from .models import Player


class PlayerListAPIView(ListAPIView):
    serializer_class = PlayerListSerializer
    permission_classes = [AllowAny]
    pagination_class = PlayerLimitOffsetPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['first_name', 'last_name', 'position', 'shirt_number']

    def get_queryset(self):
        query_list = Player.objects.all()
        query = self.request.GET.get('q')
        if query:
            query_list = query_list.filter(Q(first_name__icontains=query) |
                                           Q(last_name__icontains=query) |
                                           Q(position__icontains=query))

        return query_list


class PlayerCreateAPIView(CreateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerCreateSerializer
    permission_classes = [IsAuthenticated]


class PlayerDetailAPIView(RetrieveAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerCreateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class PlayerUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerUpdateDeleteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
