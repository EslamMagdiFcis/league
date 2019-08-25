from django.db.models import Q

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .serializers import PlayerSerializer
from .pagination import PlayerLimitOffsetPagination
from .models import Player


class PlayerListCreateAPIView(ListCreateAPIView):
    serializer_class = PlayerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
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


class PlayerDetailUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
