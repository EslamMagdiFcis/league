from rest_framework.serializers import HyperlinkedIdentityField, ModelSerializer, SerializerMethodField

from .models import Trainer


class TrainerListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(view_name='trainers-api:detail')
    team = SerializerMethodField()
    title = SerializerMethodField()

    class Meta:
        model = Trainer
        fields = ['url', 'id', 'first_name', 'last_name', 'gender', 'birth_date', 'title', 'team']

    def get_team(self, obj):
        return obj.team.name if obj.team else ''

    def get_title(self, obj):
        for short_title in obj.SHORT_TITLES:
            if short_title[0] == obj.title:
                return short_title[1]

        return ''


class TrainerDetailSerializer(ModelSerializer):
    class Meta:
        model = Trainer
        fields = ['first_name',
                  'last_name',
                  'gender',
                  'birth_date',
                  'title',
                  'team']
