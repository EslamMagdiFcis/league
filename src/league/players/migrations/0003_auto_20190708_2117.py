# Generated by Django 2.2.3 on 2019-07-08 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('players', '0002_auto_20190707_2149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='gender',
            field=models.CharField(choices=[('m', 'Male'), ('f', 'Female')], default='m', max_length=1),
        ),
    ]