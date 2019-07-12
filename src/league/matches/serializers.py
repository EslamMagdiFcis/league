from rest_framework.serializers import HyperlinkedIdentityField, ModelSerializer, SerializerMethodField

from team_stats.serializers import TeamStatsDetailSerializer

from .models import Match


class MatchListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(view_name='matches-api:detail-delete')
    team = SerializerMethodField()
    guest_team = SerializerMethodField()
    score = SerializerMethodField()

    class Meta:
        model = Match
        fields = ['url', 'id', 'team', 'guest_team', 'date', 'time', 'score']

    def get_team(self, obj):
        return obj.team.team.name if obj.team.team else ''

    def get_guest_team(self, obj):
        return obj.guest_team.team.name if obj.guest_team.team else ''

    def get_score(self, obj):
        return '{} Vs {}'.format(obj.team.goals, obj.guest_team.goals)


class MatchDetailSerializer(ModelSerializer):
    team = SerializerMethodField()
    guest_team = SerializerMethodField()

    class Meta:
        model = Match
        fields = ['team',
                  'guest_team',
                  'date',
                  'time', ]

    def get_team(self, obj):
        return TeamStatsDetailSerializer([obj.team], many=True).data

    def get_guest_team(self, obj):
        return TeamStatsDetailSerializer([obj.guest_team], many=True).data


class MatchCreateUpdateDeleteSerializer(ModelSerializer):
    class Meta:
        model = Match
        fields = ['team', 'guest_team', 'date', 'time', ]
