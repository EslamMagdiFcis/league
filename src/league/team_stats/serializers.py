from rest_framework.serializers import HyperlinkedIdentityField, ModelSerializer, SerializerMethodField

from .models import TeamStats


class TeamStatsListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(view_name='team-stats-api:detail-delete')
    team = SerializerMethodField()

    class Meta:
        model = TeamStats
        fields = ['url', 'id', 'team', 'goals', 'possession']

    def get_team(self, obj):
        return obj.team.name if obj.team else ''


class TeamStatsDetailSerializer(ModelSerializer):
    team = SerializerMethodField()

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
                  ]

    def get_team(self, obj):
        return obj.team.name


class TeamStatsCreateUpdateDeleteSerializer(ModelSerializer):
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
                  ]
