from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect

# Create your models here.

class Organization(models.Model):
    name = models.CharField(max_length=50)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    
    pub_time = models.DateTimeField(auto_now_add=True, null = True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("orgvote:Organizations")

class Topic(models.Model):
    name = models.CharField(max_length=50)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    pub_time = models.DateTimeField(auto_now_add=True, null = True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse("orgvote:home")

class Survey(models.Model):
    name = models.CharField(max_length=50) 
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    pub_time = models.DateTimeField(auto_now_add=True, null = True)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("orgvote:home")

class Question(models.Model):
    name = models.CharField(max_length=50, default="question")
    pub_time = models.DateTimeField(auto_now_add=True, null = True)

    question_text = models.TextField() 
    survey = models.ForeignKey(Survey, on_delete=models.CASCADE)

    choice1 = models.CharField(max_length=50)
    choice1_votes = models.IntegerField(default=0)

    choice2 = models.CharField(max_length=50)
    choice2_votes = models.IntegerField(default=0)

    choice3 = models.CharField(max_length=50)
    choice3_votes = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("orgvote:home")


# class Choice(models.Model):
#     choice_text= models.CharField() 
#     question = models.ForeignKey(Organization, on_delete=models.CASCADE)
#     votes = models.IntegerField(default=0)