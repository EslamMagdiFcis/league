from django.db import models

from players.models import Person


class Trainer(Person):
    SHORT_TITLES = (
        ('M', 'Manager'),
        ('GM', 'General Manager'),
    )

    title = models.CharField(max_length=3, choices=SHORT_TITLES)

    def __str__(self):
        return '{} - {}'.format(super(Trainer, self).__str__(), self.title)
