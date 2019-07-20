from django.db import models

# Create your models here.
class Country(models.Model):
    """
    model for country dropdown in html pages
    """
    country = models.CharField(max_length=200)

    def __str__(self):
        return self.country

class Category(models.Model):
    """
    model for category dropdown in html pages
    """
    category = models.CharField(max_length=200)

    def __str__(self):
        return self.category

class State(models.Model):
    """
    model for state dropdown in html pages
    """
    state = models.CharField(max_length=200)

    def __str__(self):
        return self.state

class ResearchArea(models.Model):
    """
    model for research area dropdown in html pages
    """
    research_area = models.CharField(max_length=200)

    def __str__(self):
        return self.research_area

class UGDiscipline(models.Model):
    """
    model for ug discipline dropdown in html pages
    """
    ug_discipline = models.CharField(max_length=200)

    def __str__(self):
        return self.ug_discipline

class PGDiscipline(models.Model):
    """
    model for pg discipline dropdown in html pages
    """
    pg_discipline = models.CharField(max_length=200)

    def __str__(self):
        return self.pg_discipline

class BranchQualifyingExamination(models.Model):
    """
    model for branch qualifying examination dropdown in html pages
    """
    branch = models.CharField(max_length=200)

    def __str__(self):
        return self.branch

class TypeOfWork(models.Model):
    """
    model for type of work dropdown in html pages
    """
    type_of_work = models.CharField(max_length=200)

    def __str__(self):
        return self.type_of_work
