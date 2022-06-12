from django.urls import path
from tychy.views import FlatListAll, FlatListToday, FlatListFilter
from tychy.services.flat_actions import remove_flats

urlpatterns = [
    path("list/all", FlatListAll.as_view()),
    path("list/today", FlatListToday.as_view()),
    path("filter/today", FlatListFilter.as_view()),
    path("remove/today", remove_flats),
]
