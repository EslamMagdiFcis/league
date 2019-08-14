from rest_framework.serializers import ModelSerializer

from .models import Team


class TeamListSerializer(ModelSerializer):

    class Meta:
        model = Team
        fields = ['id', 'name', 'rank', 'points']


class TeamCreateSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = ['name', 'rank', 'points']
