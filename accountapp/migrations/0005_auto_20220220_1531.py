# Generated by Django 3.0.14 on 2022-02-20 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountapp', '0004_auto_20220220_0921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appuser',
            name='FCM_token',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
