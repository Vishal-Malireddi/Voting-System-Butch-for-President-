from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, DetailView, TemplateView
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import QuestionModelForm, TopicModelForm, SurveyModelForm, OrganizationModelForm
from .models import Question, Topic, Survey, Organization 

# Create your views here.
def index(request):
    return HttpResponse("Hello World. this is the orgvote app")

class HomePageView(LoginRequiredMixin,TemplateView):
    template_name = 'orgvote/home.html'

class OrganizationListView(LoginRequiredMixin,ListView):
    model = Organization
    template_name = "orgvote/organizations.html"
    

class QuestionCreateView(LoginRequiredMixin,CreateView):
    template_name = "orgvote/create.html"
    form_class = QuestionModelForm
    queryset = Question.objects.all()

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class TopicCreateView(LoginRequiredMixin,CreateView):
    template_name = "orgvote/create.html"
    form_class = TopicModelForm
    queryset = Topic.objects.all()
    
class SurveyCreateView(LoginRequiredMixin, CreateView):
    template_name = "orgvote/create.html"
    form_class = SurveyModelForm
    queryset = Survey.objects.all()

class OrganizationCreateView(LoginRequiredMixin, CreateView):
    template_name = "orgvote/create.html"
    form_class = OrganizationModelForm
    queryset = Organization.objects.all()

class SurveyDetailView(LoginRequiredMixin,DetailView):
    template_name = "orgvote/survey-details.html"
    queryset = Survey.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Survey, id = id_) 

class TopicDetailView(LoginRequiredMixin,DetailView):
    template_name = "orgvote/topic-details.html"
    queryset = Topic.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Topic, id = id_) 

class OrganizationDetailView(LoginRequiredMixin,DetailView):
    template_name = "orgvote/organization-details.html"
    queryset = Organization.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Organization, id = id_) 

class QuestionDetailView(LoginRequiredMixin,DetailView):
    template_name = "orgvote/question-details.html" 

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(Question, id = id_) 

# inspired by code from https://github.com/PrettyPrinted/youtube_video_code.git
def vote(request, question_id):
    question = Question.objects.get(pk=question_id)
    survey_id = question.survey.id
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

        return HttpResponseRedirect(reverse('orgvote:surveyView', kwargs={'id': survey_id}))

    context = {
        'question' : question
    }
    return render(request, 'orgvote/question-vote.html', context)
