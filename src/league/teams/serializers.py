from .models import Team
from mixins.DynamicFieldsModelSerializer import DynamicFieldsModelSerializer


class TeamSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Team
        fields = ['name', 'rank', 'points', 'id']
