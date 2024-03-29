from django.db.models import Q

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import MatchSerializer
from players.pagination import PlayerLimitOffsetPagination
from .models import Match


class MatchListCreateAPIView(ListCreateAPIView):
    serializer_class = MatchSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = PlayerLimitOffsetPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['team', 'guest_team', 'date', 'time']

    def get_queryset(self):
        query_list = Match.objects.all()
        query = self.request.GET.get('q')
        if query:
            query_list = query_list.filter(Q(team__name__icontains=query) |
                                           Q(guest_team__name__icontains=query) |
                                           Q(date__icontains=query) |
                                           Q(time__icontains=query))

        return query_list


class MatchRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Match.objects.all()
    serializer_class = IsAuthenticatedOrReadOnly
    permission_classes = [IsAuthenticatedOrReadOnly]
