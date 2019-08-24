from rest_framework.serializers import HyperlinkedIdentityField, ModelSerializer, SerializerMethodField

from .models import Match


class MatchListSerializer(ModelSerializer):
    class Meta:
        model = Match
        fields = ['id', 'team', 'guest_team', 'date', 'time', ]


class MatchDetailSerializer(ModelSerializer):
    class Meta:
        model = Match
        fields = ['team',
                  'guest_team',
                  'date',
                  'time',
                  'id']
