from rest_framework.serializers import HyperlinkedIdentityField, ModelSerializer, SerializerMethodField

from .models import Trainer


class TrainerListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(view_name='trainers-api:detail')
    team = SerializerMethodField()

    class Meta:
        model = Trainer
        fields = ['url', 'id', 'first_name', 'last_name', 'title', 'team']

    def get_team(self, obj):
        return obj.team.name if obj.team else ''


class TrainerCreateSerializer(ModelSerializer):
    # team = SerializerMethodField()

    class Meta:
        model = Trainer
        fields = ['first_name',
                  'last_name',
                  'gender',
                  'birth_date',
                  'title',
                  'team']

    # def get_team(self, obj):
    #     return obj.team.name
