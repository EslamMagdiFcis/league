from django.db.models import Q

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly

from .serializers import PlayerListSerializer, PlayerDetailSerializer, PlayerCreateUpdateDeleteSerializer
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
    serializer_class = PlayerCreateUpdateDeleteSerializer
    permission_classes = [IsAuthenticated]


class PlayerDetailDeleteAPIView(DestroyModelMixin, RetrieveAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerDetailSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def delete(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)


class PlayerUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerCreateUpdateDeleteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
