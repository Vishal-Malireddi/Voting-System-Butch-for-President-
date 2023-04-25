from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, CreateView, DetailView
from .forms import QuestionModelForm
from .models import Question

# Create your views here.
def index(request):
    return HttpResponse("Hello World. this is the orgvote app")


class QuestionCreateView(CreateView):
    template_name = "orgvote/create_survey.html"
    form_class = QuestionModelForm
    queryset = Question.objects.all()