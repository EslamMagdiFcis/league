from rest_framework.serializers import HyperlinkedIdentityField, ModelSerializer, SerializerMethodField

from .models import Player


class PlayerListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(view_name='players-api:detail-delete')
    team = SerializerMethodField()

    class Meta:
        model = Player
        fields = ['url', 'id', 'first_name', 'last_name', 'position', 'shirt_number', 'team']

    def get_team(self, obj):
        return obj.team.name if obj.team else ''


class PlayerDetailSerializer(ModelSerializer):
    team = SerializerMethodField()
    gender = SerializerMethodField()
    position = SerializerMethodField()

    class Meta:
        model = Player
        fields = ['first_name',
                  'last_name',
                  'gender',
                  'birth_date',
                  'position',
                  'shirt_number',
                  'team']

    def get_team(self, obj):
        return obj.team.name

    def get_gender(self, obj):
        for short_gender in obj.SHORT_GENDER:
            if short_gender[0] == obj.gender:
                return short_gender[1]

        return ''

    def get_position(self, obj):
        for position in obj.POSITIONS:
            if position[0] == obj.position:
                return position[1]

        return ''


class PlayerCreateUpdateDeleteSerializer(ModelSerializer):

    class Meta:
        model = Player
        fields = ['first_name',
                  'last_name',
                  'gender',
                  'birth_date',
                  'position',
                  'shirt_number',
                  'team']
