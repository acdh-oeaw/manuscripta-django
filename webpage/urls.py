from django.urls import path, re_path
from . import views
from archiv.views import manuscript_as_tei_view

app_name = "webpage"


urlpatterns = [
    path("imprint", views.ImprintView.as_view(), name="imprint"),
    path("", views.GenericWebpageView.as_view(), name="start"),
    path("tei/<int:pk>", manuscript_as_tei_view, name="tei"),
    path("accounts/login/", views.user_login, name="user_login"),
    path("logout/", views.user_logout, name="user_logout"),
    path("project-info/", views.project_info, name="project_info"),
    re_path(
        r"(?P<template>[\w-]+)/",
        views.GenericWebpageView.as_view(),
        name="staticpage",
    ),
]
