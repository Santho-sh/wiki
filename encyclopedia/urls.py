from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.wiki, name="wiki"),
    path("random", views.random, name="random"),
    path("search", views.search, name="search"),
    path("create", views.create, name="create"),
    path("edit", views.edit, name="edit"),
]