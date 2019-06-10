from django.db import models
import datetime
from django.contrib.auth.models import User,AbstractBaseUser, PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.core.validators import RegexValidator

class PhdFellows(User,PermissionsMixin):
    def __str__(self):
        return self.first_name+" "+self.last_name

class Application(models.Model):
    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    # application_no = models.IntegerField(validators=[RegexValidator(regex='^.{11}$',message='Length has to be 11', code='nomatch')], unique=True)
    category_choices = [
        ('SC','SC'),
        ('OBC','OBC'),
        ('ST','ST'),
        ('EWS','EWS'),
        ('General','General'),
    ]
    category = models.CharField(choices=category_choices, default='General',max_length=10)

    having_disability = models.BooleanField(default=False)
    research_area_choices = [
        ('Machine Learning','Machine Learning'),
        ('Cloud Computing','Cloud Computing'),
        ('Airtifial Intelligence','Airtifial Intelligence'),
        ('Software Development','Software Development'),
        ('Cryptography','Cryptography'),
    ]
    research_area = models.CharField(choices=research_area_choices,max_length=50)

    enrollment_type_list = [
        ('Full time','Full time'),
        ('Part time','Part time'),
    ]
    enrollment_type = models.CharField(choices=enrollment_type_list,max_length=50)

    first_name = models.CharField(max_length=200)

    last_name = models.CharField(max_length=200)

    email = models.EmailField(max_length=200)

    date_of_birth = models.DateTimeField(datetime.date.today())

    martial_status = models.BooleanField(default=False)

    gender_list = [
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
    ]
    gender = models.CharField(choices=gender_list,max_length=20)

    phone_no = models.CharField(max_length=13)

    address = models.TextField()

    state = models.CharField(max_length=40)

    city = models.CharField(max_length=50)

    pin_code = models.IntegerField(validators=[RegexValidator(regex='^.{6}$',message='Length has to be 6', code='nomatch')])

    score_in_ug = models.FloatField()

    scale_score_list = [
        ('0-5 CGPA','0-5 CGPA',),
        ('0-10 CGPA','0-10 CGPA',),
        ('0-100%','0-100%',),
    ]
    scale_of_score_ug = models.CharField("Scale of Score",choices=scale_score_list,max_length=20)

    ug_discipline_list = [
        ('CSE','CSE'),
        ('EE','EE'),
        ('ME','ME'),
        ('ECE','ECE'),
        ('CE','CE'),
    ]
    ug_discipline = models.CharField(choices=ug_discipline_list,max_length=20)

    ug_college_or_university = models.CharField('UG College/University')

    pg_passed_or_expected_to_pass_in_year = models.IntegerField(validators=[RegexValidator(regex='^.{4}$',message='Length has to be 4', code='nomatch')])

    score_in_pg = models.FloatField()

    scale_of_score_pg = models.CharField("Scale of Score",choices=scale_score_list, max_length=20)

    pg_discipline = models.CharField(choices=ug_discipline_list,max_length=50)

    ug_college_or_university = models.CharField('UG College/University', max_length=20)

    qualifying_examination_list = [
        ("GATE","GATE"),
        ("NET","NET"),
    ]
    qualifying_examination = models.CharField(choices=qualifying_examination_list,max_length=20)

    branch_code_for_qualifying_exam = models.CharField(choices=ug_discipline_list, max_length=10)

    qualifying_exam_score_valid_upto = models.IntegerField(validators=[RegexValidator(regex='^.{4}$',message='Length has to be 4', code='nomatch')])

    all_india_rank_in_qualifying_exam = models.IntegerField()

    score_in_qualifying_exam = models.IntegerField()

    work_experience_in_year = models.IntegerField("Work Experpience(in years)")

    type_of_work_list = [
        ('Teaching','Teaching'),
        ('IT Industry','IT Industry'),
        ('Research Organisation','Research Organisation'),
        ('Other','Other'),
    ]
    type_of_work = models.CharField(choices=type_of_work_list,max_length=50)

    no_of_peer_reviewed_publications = models.IntegerField()

    no_of_patents_granted = models.IntegerField()

    guide_preference_1 = models.CharField(max_length=200)
    guide_preference_2 = models.CharField(max_length=200)
    guide_preference_3 = models.CharField(max_length=200)
