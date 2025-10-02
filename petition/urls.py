from django.urls import path
from . import views   # import the whole views module

urlpatterns = [
    path("", views.petition_page, name="petition"),
]
