# Generated by Django 3.0.14 on 2022-02-21 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountapp', '0002_auto_20220220_1804'),
    ]

    operations = [
        migrations.AddField(
            model_name='estimate',
            name='location_id',
            field=models.BigIntegerField(default=0),
        ),
    ]
