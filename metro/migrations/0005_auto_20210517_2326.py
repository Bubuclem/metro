# Generated by Django 3.2 on 2021-05-17 21:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metro', '0004_ligne_stations'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ligne',
            name='stations',
        ),
        migrations.AddField(
            model_name='ligne',
            name='stations',
            field=models.ManyToManyField(to='metro.Station'),
        ),
    ]
