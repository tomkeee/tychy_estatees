from django.urls import path
from tychy.views import (
    FlatListAll,
    FlatListToday,
    StatisticsListAll,
    StatisticsListToday,
    DistrictListView,
    StreetListView,
    StreetList,
    UpdateStatistics
)
from tychy.services.flat_actions import remove_data,remove_todays_data

urlpatterns = [
    path("list/all", FlatListAll.as_view()),
    path("list/today", FlatListToday.as_view()),
    path("statistics/all", StatisticsListAll.as_view()),
    path("statistics/today", StatisticsListToday.as_view()),
    path("districts/", DistrictListView.as_view()),
    path("streets/", StreetListView.as_view()),
    path("list/streets/", StreetList.as_view()),
    path("update/stats", UpdateStatistics.as_view()),
    path("remove/data/today", remove_todays_data),
    path("remove/data/all", remove_data),
]
