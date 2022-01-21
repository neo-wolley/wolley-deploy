from django.db import models

from dailypathapp.models import DailyPath


class Interval(models.Model):
    id = models.BigAutoField(primary_key=True, db_column='interval_id')
    daily_path = models.ForeignKey(DailyPath, on_delete=models.CASCADE, related_name='intervals')

    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    # sprint#2에 추가된 속성
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.CharField(max_length=100)

    category = models.CharField(max_length=70)
    location = models.CharField(max_length=70)

    percent = models.FloatField(default=0.0)
    EmotionType = models.TextChoices('emotion', 'positive normal negative')
    emotion = models.CharField(max_length=20, choices=EmotionType.choices, null=True)

    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'interval'

    def __str__(self):
        return f'{self.daily_path} -> (interval_id: {self.id}, category: {self.category})'

# class TimeRange(models.Model):
#     id = models.BigAutoField(primary_key=True, db_column='timerange_id')
#     interval = models.ForeignKey(DailyPath, on_delete=models.CASCADE, related_name='timeranges')
#
#     start_time = models.DateTimeField()
#     end_time = models.DateTimeField()
#
#     date_created = models.DateTimeField(auto_now_add=True)
#     last_updated = models.DateTimeField(auto_now=True)
#
#     class Meta:
#         db_table = 'timerange'
#
#     def __str__(self):
#         return f'{self.interval} -> (timerange_id :{self.id}, start2end : {self.start_time}-{self.end_time})'
