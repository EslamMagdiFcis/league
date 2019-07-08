from rest_framework.serializers import HyperlinkedIdentityField, ModelSerializer

from .models import Trainer


class TrainerListSerializer(ModelSerializer):
    url = HyperlinkedIdentityField(view_name='trainers-api:detail')

    class Meta:
        model = Trainer
        fields = ['url', 'id', 'first_name', 'last_name', 'title']


class TrainerCreateSerializer(ModelSerializer):
    class Meta:
        model = Trainer
        fields = ['first_name',
                  'last_name',
                  'gender',
                  'birth_date',
                  'title']
