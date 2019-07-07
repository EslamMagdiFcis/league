from rest_framework.serializers import HyperlinkedIdentityField, ModelSerializer

from .models import Player


class PlayerListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(view_name='players-api:detail')

    class Meta:
        model = Player
        fields = ['url', 'id', 'first_name', 'last_name', 'position', 'shirt_number']


class PlayerCreateSerializer(ModelSerializer):
    class Meta:
        model = Player
        fields = ['first_name',
                  'last_name',
                  'gender',
                  'birth_date',
                  'position',
                  'shirt_number']
