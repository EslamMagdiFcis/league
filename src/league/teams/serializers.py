from rest_framework.serializers import HyperlinkedIdentityField, ModelSerializer

from .models import Team


class TeamListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(view_name='teams-api:detail')

    class Meta:
        model = Team
        fields = ['url', 'id', 'name']


class TeamCreateSerializer(ModelSerializer):
    class Meta:
        model = Team
        fields = ['name', 'rank', 'points']
