from django.urls import path, include
from . import views

urlpatterns = [
    path("contact", views.contact_view, name="contact"),
    path("team", views.team_view, name="team"),
    path("", views.services_view, name="services"),
]
