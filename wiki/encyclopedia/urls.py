from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("/createnewpage", views.createnewpage, name="createnewpage"),
    path("{/entrypage/<str:title>}", views.displayentry, name="displayentry"),
    path("/randomenrty", views.randomentry, name="randomentry"),
    path("{/updateentry/<str:title>}", views.updateentry, name="updateentry"),
    path("{/search}", views.search, name="search")
]
