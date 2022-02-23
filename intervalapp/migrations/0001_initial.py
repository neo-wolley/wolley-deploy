# Generated by Django 3.0.14 on 2022-02-24 02:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('dailypathapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='IntervalStay',
            fields=[
                ('id', models.BigAutoField(db_column='intervalstay_id', primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('address', models.CharField(max_length=100)),
                ('category', models.CharField(max_length=70)),
                ('location', models.CharField(max_length=70)),
                ('location_id', models.CharField(default='0', max_length=100)),
                ('percent', models.FloatField(default=0.0)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('daily_path', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='intervalstays', to='dailypathapp.DailyPath')),
            ],
            options={
                'db_table': 'intervalstay',
            },
        ),
        migrations.CreateModel(
            name='IntervalMove',
            fields=[
                ('id', models.BigAutoField(db_column='intervalmove_id', primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
                ('transport', models.CharField(max_length=70)),
                ('percent', models.FloatField(default=0.0)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('daily_path', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='intervalmoves', to='dailypathapp.DailyPath')),
            ],
            options={
                'db_table': 'intervalmove',
            },
        ),
    ]
