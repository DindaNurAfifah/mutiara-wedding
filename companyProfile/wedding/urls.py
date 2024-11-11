<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
    path("Team/", views.team, name="team")
]
=======
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.contact_view, name="contact"),
]
>>>>>>> 50c2b05d77617833c97528e9f82746332b9f9372
