from django.db import models

# Create your models here.
class Country(models.Model):
    country = models.CharField(max_length=200)

    def __str__(self):
        return self.country

class Category(models.Model):
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category

class State(models.Model):
    state = models.CharField(max_length=200)

    def __str__(self):
        return self.state

class ResearchArea(models.Model):
    research_area = models.CharField(max_length=200)

    def __str__(self):
        return self.research_area

class UGDiscipline(models.Model):
    ug_discipline = models.CharField(max_length=200)

    def __str__(self):
        return self.ug_discipline

class PGDiscipline(models.Model):
    pg_discipline = models.CharField(max_length=200)

    def __str__(self):
        return self.pg_discipline

class BranchQualifyingExamination(models.Model):
    branch = models.CharField(max_length=200)

    def __str__(self):
        return self.branch

class TypeOfWork(models.Model):
    type_of_work = models.CharField(max_length=200)

    def __str__(self):
        return self.type_of_work
