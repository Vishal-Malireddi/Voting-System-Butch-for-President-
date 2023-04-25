from django.urls import path
from . import views
from .views import QuestionCreateView

# define the urls that will be used under the orgvote/ domain
urlpatterns = [
    path("create-question/", QuestionCreateView.as_view(), name="index"),
]

