from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DetailView

from .forms import QuestionModelForm, TopicModelForm, SurveyModelForm, OrganizationModelForm, HomeModelForm
from .models import Question, Topic, Survey, Organization, Home

# Create your views here.
def index(request):
    return HttpResponse("Hello World. this is the orgvote app")

class HomeCreateView(CreateView):
    template_name = "orgvote/create.html"
    form_class = HomeModelForm
    queryset = Home.objects.all()

class QuestionCreateView(CreateView):
    template_name = "orgvote/create.html"
    form_class = QuestionModelForm
    queryset = Question.objects.all()

class TopicCreateView(CreateView):
    template_name = "orgvote/create.html"
    form_class = TopicModelForm
    queryset = Topic.objects.all()
    
class SurveyCreateView(CreateView):
    template_name = "orgvote/create.html"
    form_class = SurveyModelForm
    queryset = Survey.objects.all()

class OrganizationCreateView(CreateView):
    template_name = "orgvote/create.html"
    form_class = OrganizationModelForm
    queryset = Organization.objects.all()

class SurveyDetailView(DetailView):
    template_name = "orgvote/survey-details.html"
    queryset = Survey.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Survey, id = id_) 

class TopicDetailView(DetailView):
    template_name = "orgvote/topic-details.html"
    queryset = Topic.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Topic, id = id_) 

class OrganizationDetailView(DetailView):
    template_name = "orgvote/organization-details.html"
    queryset = Organization.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Organization, id = id_) 

class QuestionDetailView(DetailView):
    template_name = "orgvote/question-details.html" 

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Question, id = id_) 