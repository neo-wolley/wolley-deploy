# Generated by Django 3.0.14 on 2022-01-13 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
