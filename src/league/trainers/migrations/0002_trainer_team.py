# Generated by Django 2.2.3 on 2019-07-08 22:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0001_initial'),
        ('trainers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='trainer',
            name='team',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='teams.Team'),
        ),
    ]
