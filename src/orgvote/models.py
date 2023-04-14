from django.db import models

# Create your models here.

class Organization(models.Model):
    name = models.CharField()

class Topic(models.Model):
    name = models.CharField()
    org = models.ForeignKey(Organization, on_delete=models.CASCADE)

class Survey(models.Model):
    name = models.CharField() 
    topic = models.ForeignKey(Organization, on_delete=models.CASCADE)

class Question(models.Model):
    question_text = models.CharField() 
    survey = models.ForeignKey(Organization, on_delete=models.CASCADE)

class Choice(models.Model):
    choice_text= models.CharField() 
    question = models.ForeignKey(Organization, on_delete=models.CASCADE)
    votes = models.IntegerField(default=0)