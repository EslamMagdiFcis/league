from rest_framework.serializers import HyperlinkedIdentityField, ModelSerializer, SerializerMethodField

from .models import Player


class PlayerListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(view_name='players-api:detail')
    team = SerializerMethodField()

    class Meta:
        model = Player
        fields = ['url', 'id', 'first_name', 'last_name', 'position', 'shirt_number', 'team']

    def get_team(self, obj):
        return obj.team.name if obj.team else ''


class PlayerCreateSerializer(ModelSerializer):
    # team = SerializerMethodField()

    class Meta:
        model = Player
        fields = ['first_name',
                  'last_name',
                  'gender',
                  'birth_date',
                  'position',
                  'shirt_number',
                  'team']

    # def get_team(self, obj):
    #     return obj.team.name
