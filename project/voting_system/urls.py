from django.urls import path
from . import views

# define the urls that will be used under the voting_system/ domain
urlpatterns = [
    path("", views.index, name="index"),


]
