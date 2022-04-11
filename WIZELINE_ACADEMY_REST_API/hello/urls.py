from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("external", views.external, name="external")
    ]