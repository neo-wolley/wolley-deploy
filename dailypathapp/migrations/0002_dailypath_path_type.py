# Generated by Django 3.0.14 on 2022-02-24 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailypathapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dailypath',
            name='path_type',
            field=models.CharField(default='daily', max_length=10),
        ),
    ]
