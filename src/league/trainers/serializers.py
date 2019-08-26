from rest_framework.serializers import ModelSerializer

from .models import Trainer


class TrainerSerializer(ModelSerializer):
    class Meta:
        model = Trainer
        fields = ['id', 'first_name', 'last_name', 'gender', 'birth_date', 'title', 'team']