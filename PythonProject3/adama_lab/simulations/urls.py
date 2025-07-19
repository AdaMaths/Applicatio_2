from django.urls import path
from . import views

from .views import laser_view

from .views import calculs_view

from .views import data_science_view

urlpatterns = [
    path("navier/", views.navier_view, name="navier"),
]



urlpatterns += [
    path("laser/", laser_view, name="laser"),
]




urlpatterns += [
    path("calculs/", calculs_view, name="calculs"),
]




urlpatterns += [
    path("data-science/", data_science_view, name="data_science"),
]