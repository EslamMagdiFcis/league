from django.db.models import Q

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import TeamSerializer
from players.pagination import PlayerLimitOffsetPagination
from .models import Team


class TeamListCreateAPIView(ListCreateAPIView):
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = PlayerLimitOffsetPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']

    def get_queryset(self):
        query_list = Team.objects.all()
        query = self.request.GET.get('q')
        if query:
            query_list = query_list.filter(Q(name__icontains=query))

        return query_list


class TeamDetailUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
