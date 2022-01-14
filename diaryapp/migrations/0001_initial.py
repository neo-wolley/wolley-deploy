# Generated by Django 3.0.14 on 2022-01-14 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dailypathapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Diary',
            fields=[
                ('id', models.BigAutoField(db_column='diary_id', primary_key=True, serialize=False)),
                ('content', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('pie_chart', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dailypathapp.DailyPath')),
            ],
            options={
                'db_table': 'diary',
            },
        ),
    ]
