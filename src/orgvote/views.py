from django.shortcuts import render, get_object_or_404
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

# inspired by code from https://github.com/PrettyPrinted/youtube_video_code.git
def vote(request, question_id):
    question = Question.objects.get(pk=question_id)

    if request.method == 'POST':

        selected_option = request.POST['question']
        if selected_option == 'choice1':
            question.choice1_votes+= 1
        elif selected_option == 'choice2':
            question.choice2_votes+= 1
        elif selected_option == 'choice3':
            question.choice3_votes+= 1
        else:
            return HttpResponse(400, 'Invalid form')

        question.save()

        return redirect('results', question.id)

    context = {
        'question' : question
    }
    return render(request, 'orgvote/question-vote.html', context)
