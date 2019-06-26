from django.db import models
from accounts.models import User
from datetime import date
from django.utils.translation import gettext as _
from django.core.validators import RegexValidator

class Application(models.Model):

    user = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    category_choices = [
        ('','Select'),
        ('SC','SC'),
        ('OBC','OBC'),
        ('ST','ST'),
        ('EWS','EWS'),
        ('General','General'),
    ]
    category = models.CharField(choices=category_choices, default='Select',max_length=10)

    having_disability = models.BooleanField("Disabled",default=False)
    research_area_choices = [
        ('','Select'),
        ('Machine Learning','Machine Learning'),
        ('Cloud Computing','Cloud Computing'),
        ('Airtifial Intelligence','Airtifial Intelligence'),
        ('Software Development','Software Development'),
        ('Cryptography','Cryptography'),
    ]
    research_area = models.CharField(default='Select',choices=research_area_choices,max_length=50)

    applying_for_list = [
        ('','Select'),
        ('PhD','PhD'),
        ('MS','MS'),
    ]
    applying_for = models.CharField(choices=applying_for_list,default='Select',max_length=5)

    enrollment_type_list = [
        ('','Select'),
        ('Full time','Full time'),
        ('Part time','Part time'),
    ]
    enrollment_type = models.CharField(default='Select',choices=enrollment_type_list,max_length=50)

    first_name = models.CharField(max_length=200)

    last_name = models.CharField(max_length=200)

    email = models.EmailField(max_length=200)

    date_of_birth = models.CharField("Date of Birth",null=True,max_length=10)

    married = models.BooleanField(default=False)

    gender_list = [
        ('','Select'),
        ('Male','Male'),
        ('Female','Female'),
        ('Other','Other'),
    ]
    gender = models.CharField(default='Select',choices=gender_list,max_length=20)

    phone_no = models.CharField("Phone Number(With Country Code)",max_length=13)

    address = models.TextField()

    country = models.CharField(max_length=200)

    state = models.CharField(null=True,max_length=200)

    city = models.CharField(max_length=200)

    pin_code = models.CharField(validators=[RegexValidator(regex='^.{6}$',message='Length has to be 6', code='nomatch')],max_length=6)

    score_in_ug = models.FloatField("Score in UG",default=None ,null=True)

    scale_score_list = [
        ('','Select'),
        ('0-5 CGPA','0-5 CGPA',),
        ('0-10 CGPA','0-10 CGPA',),
        ('0-100%','0-100%',),
    ]
    scale_of_score_ug = models.CharField("Scale of Score",default='Select',choices=scale_score_list,max_length=20)

    ug_discipline_list = [
        ('','Select'),
        ('CSE','CSE'),
        ('EE','EE'),
        ('ME','ME'),
        ('ECE','ECE'),
        ('CE','CE'),
    ]
    ug_discipline = models.CharField("UG Discipline",default='Select',choices=ug_discipline_list,max_length=20)

    ug_college_or_university = models.CharField('UG College/University',max_length=200)

    pg_passed_or_expected_to_pass_in_year = models.IntegerField("PG Passed Year or Expected to Pass in Year",validators=[RegexValidator(regex='^.{4}$',message='Length has to be 4',code='nomatch')],default=None ,null=True)

    score_in_pg = models.FloatField("Score in PG", default=None ,null=True)

    scale_of_score_pg = models.CharField("Scale of Score",default='Select',choices=scale_score_list, max_length=20)

    pg_discipline = models.CharField("PG Discipline",default='Select',choices=ug_discipline_list,max_length=50)

    pg_college_or_university = models.CharField('PG College/University', max_length=200)

    qualifying_examination_list = [
        ('','Select'),
        ("GATE","GATE"),
        ("NET","NET"),
    ]
    qualifying_examination = models.CharField(default='Select',choices=qualifying_examination_list,max_length=20)

    branch_code_for_qualifying_exam = models.CharField(default='Select',choices=ug_discipline_list, max_length=10)

    qualifying_exam_score_valid_upto = models.IntegerField(validators=[RegexValidator(regex='^.{4}$',message='Length has to be 4', code='nomatch')],default=None ,null=True)

    all_india_rank_in_qualifying_exam = models.IntegerField("All India rank in Qualifying Exam",default=None ,null=True)

    score_in_qualifying_exam = models.FloatField(default=None ,null=True)

    work_experience_in_year = models.IntegerField("Work Experpience(in years)",default=0 ,null=True)

    type_of_work_list = [
        ('','Select'),
        ('Teaching','Teaching'),
        ('IT Industry','IT Industry'),
        ('Research Organisation','Research Organisation'),
        ('Other','Other'),
    ]
    type_of_work = models.CharField(default='Select',choices=type_of_work_list,max_length=50)

    no_of_peer_reviewed_publications = models.IntegerField(default=0 ,null=True)

    no_of_patents_granted = models.IntegerField(default=0 ,null=True)

    guide_preference_1 = models.CharField(max_length=200)
    guide_preference_2 = models.CharField(max_length=200)
    guide_preference_3 = models.CharField(max_length=200)

    status_list = [
        ('Draft','Draft'),
        ('Submitted','Submitted'),
        ('Shortlisted for Test','Shortlisted for Test'),
        ('Shortlisted for Interview','Shortlisted for Interview'),
        ('Selected','Selected'),
        ('Rejected','Rejected'),
    ]
    current_status = models.CharField(default='Draft',choices=status_list,max_length=30)

    submitted_at = models.DateField(blank=True,null=True)

    submitted_year = models.CharField(max_length=4)

    application_no = models.IntegerField(unique=True,default=None ,null=True)

    was_selected_for_interview = models.BooleanField(default=False)

    def __str__(self):
        return str(self.application_no)

    class Meta:
        ordering = ('-submitted_at',)
        # unique_together = ('submitted_year','applying_for','email')

class WrittenTestScore(models.Model):
    application_no = models.OneToOneField(Application,on_delete=models.CASCADE)
    written_test_score = models.IntegerField(null=True)
    programming_test_score = models.IntegerField(null=True)

    def __str__(self):
        return str(self.application_no)
