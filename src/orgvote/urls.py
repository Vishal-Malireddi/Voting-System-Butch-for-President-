from django.urls import path
from . import views

# define the urls that will be used under the orgvote/ domain
urlpatterns = [
    path("", views.index, name="index"),
]

