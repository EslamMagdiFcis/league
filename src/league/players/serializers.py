from rest_framework.serializers import HyperlinkedIdentityField, ModelSerializer, SerializerMethodField

from .models import Player


class PlayerSerializer(ModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'first_name', 'last_name', 'gender', 'birth_date', 'position', 'shirt_number', 'team']
