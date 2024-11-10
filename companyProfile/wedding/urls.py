from django.urls import path
from . import views

urlpatterns = [
    path("Team/", views.team, name="team")
]
