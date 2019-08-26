from mixins.DynamicFieldsModelSerializer import DynamicFieldsModelSerializer

from .models import TeamStats


class TeamStatsSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = TeamStats
        fields = ['id', 'team', 'possession', 'shots', 'shots_on_target', 'passes', 'pass_accuracy', 'fouls',
                  'yellow_card', 'red_card', 'corners', 'offsides', 'goals', ]
