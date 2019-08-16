from rest_framework.serializers import HyperlinkedIdentityField, ModelSerializer, SerializerMethodField

from .models import Player


class PlayerListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(view_name='players-api:detail-delete')
    team = SerializerMethodField()
    position = SerializerMethodField()

    class Meta:
        model = Player
        fields = ['url', 'id', 'first_name', 'last_name', 'gender', 'birth_date', 'position', 'shirt_number', 'team']

    def get_team(self, obj):
        return obj.team.name if obj.team else ''

    def get_position(self, obj):
        for position in obj.POSITIONS:
            if position[0] == obj.position:
                return position[1]

        return ''


class PlayerDetailSerializer(ModelSerializer):
    class Meta:
        model = Player
        fields = ['first_name',
                  'last_name',
                  'gender',
                  'birth_date',
                  'position',
                  'shirt_number',
                  'team']
