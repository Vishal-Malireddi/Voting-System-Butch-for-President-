from django.urls import path
from . import views
from .views import QuestionCreateView, TopicCreateView, SurveyCreateView, OrganizationCreateView, SurveyListView

# define the urls that will be used under the orgvote/ domain
urlpatterns = [
    path("create-question/", QuestionCreateView.as_view(), name="createQuestion"),
    path("create-topic/", TopicCreateView.as_view(), name="createTopic"),
    path("create-survey/", SurveyCreateView.as_view(), name="createSurvey"),
    path("create-organization/", OrganizationCreateView.as_view(), name="createOrganization"),
    path("survey-view/", SurveyListView.as_view(), name="surveyView")
]

