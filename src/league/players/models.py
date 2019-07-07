from django.db import models


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    SHORT_GENDER = (
        ('m', 'Male'),
        ('f', 'Female')
    )
    gender = models.CharField(max_length=1, choices=SHORT_GENDER, default='m')
    birth_date = models.DateField()


class Player(Person):
    POSITIONS = (
        ('GK', 'Goalkeeper'),
        ('FB', 'Full-Back'),
        ('WB', 'Wing-Back'),
        ('CD', 'Central Defender'),
        ('CC', 'Centre Back'),
        ('S', 'Sweeper'),
        ('CM', 'Central Midfield'),
        ('WM', 'Wide Midfield'),
        ('WW', 'Wide Winger'),
        ('SF', 'Striker Forward'),
        ('CF', 'Centre Forward'),
        ('CF', 'Centre Forward'),
    )
    position = models.CharField(max_length=10, choices=POSITIONS, default='FB')
    shirt_number = models.IntegerField()
