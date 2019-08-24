from django.db.models import Q

from rest_framework.generics import (CreateAPIView,
                                     ListAPIView,
                                     RetrieveUpdateDestroyAPIView,
                                     RetrieveUpdateAPIView,
                                     RetrieveDestroyAPIView)

from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly

from .serializers import TeamStatsListSerializer, TeamStatsCreateUpdateDeleteSerializer
from players.pagination import PlayerLimitOffsetPagination
from .models import TeamStats


class TeamStatsListAPIView(ListAPIView):
    serializer_class = TeamStatsCreateUpdateDeleteSerializer
    permission_classes = [AllowAny]
    pagination_class = PlayerLimitOffsetPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['team']

    def get_queryset(self):
        query_list = TeamStats.objects.all()
        query = self.request.GET.get('q')
        if query:
            query_list = query_list.filter(Q(team__name__icontains=query))

        return query_list


class TeamStatsCreateAPIView(CreateAPIView):
    queryset = TeamStats.objects.all()
    serializer_class = TeamStatsCreateUpdateDeleteSerializer
    permission_classes = [IsAuthenticated]


class TeamStatsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = TeamStats.objects.all()
    serializer_class = TeamStatsCreateUpdateDeleteSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
