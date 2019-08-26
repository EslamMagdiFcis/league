from mixins.DynamicFieldsModelSerializer import DynamicFieldsModelSerializer

from .models import Match


class MatchSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Match
        fields = ['id', 'team', 'guest_team', 'date', 'time', ]
