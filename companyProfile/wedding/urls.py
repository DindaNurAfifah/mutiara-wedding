from django.urls import path, include
from . import views

urlpatterns = [
    path("contact/", views.contact_view, name="contact"),
    path("team/", views.team_view, name="team"),
    path("about/", views.about_view, name="about"),
    path("gallery/", views.gallery_view, name="gallery"),
    path("services/", views.services_view, name="services"),
    path("", views.home_view, name="homepage"),
]
