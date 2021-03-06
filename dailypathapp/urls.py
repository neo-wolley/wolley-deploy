from django.urls import path
from .views import PathDailyRequestView, MonthlyRequestView, PieChartRequestView, MapRequestView, MapLogRequestView, \
    WeeklyRequestView, YearlyRequestView, PathListRequestView, PathPastRequestView

app_name = "dailypathapp"

urlpatterns = [
    path('path/daily/', PathDailyRequestView.as_view(), name="pathdaily_request"),
    path('path/list/', PathListRequestView.as_view(), name="path_list_request"),
    path('path/past/', PathPastRequestView.as_view(), name="path_past_request"),

    path('weekly/', WeeklyRequestView.as_view(), name="weekly_request"),
    path('monthly/', MonthlyRequestView.as_view(), name="monthly_request"),
    path('yearly/', YearlyRequestView.as_view(), name="yearly_request"),
    path('piechart/', PieChartRequestView.as_view(),name="piechart_request"),
    path('map/', MapRequestView.as_view(), name="map_request"),
    path('map/log/', MapLogRequestView.as_view(), name="map_log_request"),
]
