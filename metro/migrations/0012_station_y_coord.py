# Generated by Django 3.2 on 2021-05-18 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metro', '0011_station_x_coord'),
    ]

    operations = [
        migrations.AddField(
            model_name='station',
            name='y_coord',
            field=models.IntegerField(null=True),
        ),
    ]