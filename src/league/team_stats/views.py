from django.db.models import Q

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import TeamStatsSerializer
from players.pagination import PlayerLimitOffsetPagination
from .models import TeamStats


class TeamStatsListCreateAPIView(ListCreateAPIView):
    serializer_class = TeamStatsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = PlayerLimitOffsetPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['team']

    def get_queryset(self):
        query_list = TeamStats.objects.all()
        query = self.request.GET.get('q')
        if query:
            query_list = query_list.filter(Q(team__name__icontains=query))

        return query_list


class TeamStatsRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = TeamStats.objects.all()
    serializer_class = TeamStatsSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
