from django.db import models

# Create your models here.

class Organization(models.Model):
    name = models.CharField()

class Topic(models.Model):
    name = models.CharField()

class Survey(models.Model):
    name = models.CharField() 

class (models.Model):
    pass
