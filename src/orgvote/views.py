from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DetailView

from .forms import QuestionModelForm, TopicModelForm, SurveyModelForm, OrganizationModelForm
from .models import Question, Topic, Survey, Organization

# Create your views here.
def index(request):
    return HttpResponse("Hello World. this is the orgvote app")


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

class SurveyListView(ListView):
    template_name = "orgvote/detail.html"
    queryset = Survey.objects.all()