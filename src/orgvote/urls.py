from django.urls import path
from . import views
from .views import QuestionCreateView, TopicCreateView, SurveyCreateView, OrganizationCreateView, SurveyDetailView, QuestionDetailView, TopicDetailView, OrganizationDetailView, vote, HomePageView

# define the urls that will be used under the orgvote/ domain
app_name = "orgvote"
urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("create-question/", QuestionCreateView.as_view(), name="createQuestion"),
    path("create-topic/", TopicCreateView.as_view(), name="createTopic"),
    path("create-survey/", SurveyCreateView.as_view(), name="createSurvey"),
    path("create-organization/", OrganizationCreateView.as_view(), name="createOrganization"),
    path("survey-details<int:id>/", SurveyDetailView.as_view(), name="surveyView"),
    # path("question-details<int:id>/", QuestionDetailView.as_view(), name="questionView"),
    path("topic-details<int:id>/", TopicDetailView.as_view(), name="topicView"),
    path("organization-details<int:id>/", OrganizationDetailView.as_view(), name="organizationView"),
    path("question-vote<question_id>/", vote, name='questionVote')
]

