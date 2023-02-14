from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.wiki, name="wiki"),
    path("search", views.search, name="search"),
]

# this id django path - path("wiki/<str:title>", views.wiki, name="wiki")
# link this url in templates file 