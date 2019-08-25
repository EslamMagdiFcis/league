from mixins.DynamicFieldsModelSerializer import DynamicFieldsModelSerializer

from .models import Player


class PlayerSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = Player
        fields = ['id', 'first_name', 'last_name', 'gender', 'birth_date', 'position', 'shirt_number', 'team']
