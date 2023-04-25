from django import forms

from .models import Question

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