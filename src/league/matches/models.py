from django.db import models

from team_stats.models import TeamStats


class Match(models.Model):
    team = models.ForeignKey(TeamStats, null=True, on_delete=models.SET_NULL)
    guest_team = models.ForeignKey(TeamStats, null=True, on_delete=models.SET_NULL, related_name='guest_team_set')
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return '{} Vs {} , Day: {}, AT: {}'.format(self.team, self.guest_team, self.date, self.time)
