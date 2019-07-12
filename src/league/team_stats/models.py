from django.db import models

from teams.models import Team


class TeamStats(models.Model):
    team = models.ForeignKey(Team, null=True, on_delete=models.SET_NULL)
    possession = models.IntegerField()
    shots = models.IntegerField()
    shots_on_target = models.IntegerField()
    passes = models.IntegerField()
    pass_accuracy = models.IntegerField()
    fouls = models.IntegerField()
    yellow_card = models.IntegerField()
    red_card = models.IntegerField()
    corners = models.IntegerField()
    offsides = models.IntegerField()
    goals = models.IntegerField()

    def __str__(self):
        return '{} score {}'.format(self.team.name, self.goals)
