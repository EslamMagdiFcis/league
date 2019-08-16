from .models import Team
from mixins.DynamicFieldsModelSerializer import DynamicFieldsModelSerializer


class TeamListSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Team
        fields = ['name', 'rank', 'points', 'id']


class TeamCreateSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Team
        fields = ['name', 'rank', 'points']
