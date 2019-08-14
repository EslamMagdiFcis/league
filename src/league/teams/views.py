from django.db.models import Q

from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.mixins import DestroyModelMixin, UpdateModelMixin
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework import status

from rest_framework.response import Response

from .serializers import TeamListSerializer, TeamCreateSerializer
from players.pagination import PlayerLimitOffsetPagination
from .models import Team


class TeamListAPIView(ListAPIView):
    serializer_class = TeamListSerializer
    permission_classes = [AllowAny]
    pagination_class = PlayerLimitOffsetPagination
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name']

    def get_queryset(self):
        query_list = Team.objects.all()
        query = self.request.GET.get('q')
        if query:
            query_list = query_list.filter(Q(name__icontains=query))

        return query_list


class TeamCreateAPIView(CreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamCreateSerializer
    permission_classes = [IsAuthenticated]


class TeamDetailUpdateDeleteAPIView(UpdateModelMixin, DestroyModelMixin, RetrieveAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamCreateSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
