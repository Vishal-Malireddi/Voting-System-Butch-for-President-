from django import forms

from .models import Question, Topic, Survey, Organization, Home

class HomeModelForm(forms.ModelForm):

    class Meta:
        model = Home
        fields = [
            
        ]

class QuestionModelForm(forms.ModelForm):
    class Meta:
        model = Question
        fields =[
            'name',
            'question_text',
            'survey',
            'choice1',
            'choice2',
            'choice3',
        ]

class TopicModelForm(forms.ModelForm):
    class Meta:
        model = Topic 
        fields =[
           'name',
           'organization' 
        ]

class SurveyModelForm(forms.ModelForm):
    class Meta:
        model = Survey
        fields =[
            'name',
            'topic' 
        ]

class OrganizationModelForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields =[
            'name'
        ]