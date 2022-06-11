from django.urls import path
from tychy.views import FlatListAll, FlatListToday, FlatListFilter

urlpatterns = [
    path("list/all", FlatListAll.as_view()),
    path("list/today", FlatListToday.as_view()),
    path("filter/today", FlatListFilter.as_view()),
]
