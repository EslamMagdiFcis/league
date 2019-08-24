from rest_framework.serializers import HyperlinkedIdentityField, ModelSerializer, SerializerMethodField

from mixins.DynamicFieldsModelSerializer import DynamicFieldsModelSerializer

from .models import TeamStats


class TeamStatsListSerializer(ModelSerializer):
    team = SerializerMethodField()

    class Meta:
        model = TeamStats
        fields = ['id', 'team', 'goals', 'possession']

    def get_team(self, obj):
        return obj.team.name if obj.team else ''


class TeamStatsCreateUpdateDeleteSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = TeamStats
        fields = ['team',
                  'possession',
                  'shots',
                  'shots_on_target',
                  'passes',
                  'pass_accuracy',
                  'fouls',
                  'yellow_card',
                  'red_card',
                  'corners',
                  'offsides',
                  'goals',
                  'id',
                  ]
