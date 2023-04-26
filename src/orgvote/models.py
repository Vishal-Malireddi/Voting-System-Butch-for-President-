from django.db import models

# Create your models here.

class Organization(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Topic(models.Model):
    name = models.CharField(max_length=50)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Survey(models.Model):
    name = models.CharField(max_length=50) 
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Question(models.Model):
    name = models.CharField(max_length=50, default="question")

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


# class Choice(models.Model):
#     choice_text= models.CharField() 
#     question = models.ForeignKey(Organization, on_delete=models.CASCADE)
#     votes = models.IntegerField(default=0)