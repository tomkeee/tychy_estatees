from django.urls import path
from tychy.views import (
    FlatListAll,
    FlatListToday,
    FlatListFilter,
    StatisticsListAll,
    StatisticsListToday,
    DistrictListView,
    StreetListView,
    StreetList,
)
from tychy.services.flat_actions import remove_flats

urlpatterns = [
    path("list/all", FlatListAll.as_view()),
    path("list/today", FlatListToday.as_view()),
    path("filter/today", FlatListFilter.as_view()),
    path("statistics/all", StatisticsListAll.as_view()),
    path("statistics/today", StatisticsListToday.as_view()),
    path("districts/", DistrictListView.as_view()),
    path("streets/", StreetListView.as_view()),
    path("list/streets/", StreetList.as_view()),
    path("remove/today", remove_flats),
]
