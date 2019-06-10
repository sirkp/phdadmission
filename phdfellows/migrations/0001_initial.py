# Generated by Django 2.2 on 2019-06-10 20:43

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhdFellows',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user', models.Model),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('SC', 'SC'), ('OBC', 'OBC'), ('ST', 'ST'), ('EWS', 'EWS'), ('General', 'General')], default='General', max_length=10)),
                ('having_disability', models.BooleanField(default=False, verbose_name='Disabled')),
                ('research_area', models.CharField(choices=[('Machine Learning', 'Machine Learning'), ('Cloud Computing', 'Cloud Computing'), ('Airtifial Intelligence', 'Airtifial Intelligence'), ('Software Development', 'Software Development'), ('Cryptography', 'Cryptography')], max_length=50)),
                ('applying_for', models.CharField(choices=[('PhD', 'PhD'), ('MS', 'MS')], max_length=5)),
                ('enrollment_type', models.CharField(choices=[('Full time', 'Full time'), ('Part time', 'Part time')], max_length=50)),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('date_of_birth', models.DateField(default=datetime.date.today, verbose_name='Date of Birth')),
                ('married', models.BooleanField(default=False)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], max_length=20)),
                ('phone_no', models.CharField(max_length=13, verbose_name='Phone Number(With Country Code)')),
                ('address', models.TextField()),
                ('state', models.CharField(max_length=40)),
                ('city', models.CharField(max_length=50)),
                ('pin_code', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 6', regex='^.{6}$')])),
                ('score_in_ug', models.FloatField(null=True, verbose_name='Score in UG')),
                ('scale_of_score_ug', models.CharField(choices=[('0-5 CGPA', '0-5 CGPA'), ('0-10 CGPA', '0-10 CGPA'), ('0-100%', '0-100%')], max_length=20, verbose_name='Scale of Score')),
                ('ug_discipline', models.CharField(choices=[('CSE', 'CSE'), ('EE', 'EE'), ('ME', 'ME'), ('ECE', 'ECE'), ('CE', 'CE')], max_length=20, verbose_name='UG Discipline')),
                ('ug_college_or_university', models.CharField(max_length=200, verbose_name='UG College/University')),
                ('pg_passed_or_expected_to_pass_in_year', models.IntegerField(null=True, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 4', regex='^.{4}$')], verbose_name='PG Passed Year or Expected to Pass in Year')),
                ('score_in_pg', models.FloatField(null=True, verbose_name='Score in PG')),
                ('scale_of_score_pg', models.CharField(choices=[('0-5 CGPA', '0-5 CGPA'), ('0-10 CGPA', '0-10 CGPA'), ('0-100%', '0-100%')], max_length=20, verbose_name='Scale of Score')),
                ('pg_discipline', models.CharField(choices=[('CSE', 'CSE'), ('EE', 'EE'), ('ME', 'ME'), ('ECE', 'ECE'), ('CE', 'CE')], max_length=50, verbose_name='PG Discipline')),
                ('pg_college_or_university', models.CharField(max_length=200, verbose_name='PG College/University')),
                ('qualifying_examination', models.CharField(choices=[('GATE', 'GATE'), ('NET', 'NET')], max_length=20)),
                ('branch_code_for_qualifying_exam', models.CharField(choices=[('CSE', 'CSE'), ('EE', 'EE'), ('ME', 'ME'), ('ECE', 'ECE'), ('CE', 'CE')], max_length=10)),
                ('qualifying_exam_score_valid_upto', models.IntegerField(null=True, validators=[django.core.validators.RegexValidator(code='nomatch', message='Length has to be 4', regex='^.{4}$')])),
                ('all_india_rank_in_qualifying_exam', models.IntegerField(null=True, verbose_name='All India rank in Qualifying Exam')),
                ('score_in_qualifying_exam', models.FloatField(null=True)),
                ('work_experience_in_year', models.CharField(max_length=3, verbose_name='Work Experpience(in years)')),
                ('type_of_work', models.CharField(choices=[('Teaching', 'Teaching'), ('IT Industry', 'IT Industry'), ('Research Organisation', 'Research Organisation'), ('Other', 'Other')], max_length=50)),
                ('no_of_peer_reviewed_publications', models.IntegerField(null=True)),
                ('no_of_patents_granted', models.IntegerField(null=True)),
                ('guide_preference_1', models.CharField(max_length=200)),
                ('guide_preference_2', models.CharField(max_length=200)),
                ('guide_preference_3', models.CharField(max_length=200)),
                ('current_status', models.CharField(choices=[('Draft', 'Draft'), ('Submitted', 'Submitted'), ('Shortlisted for Test', 'Shortlisted for Test'), ('Shortlisted for Interview', 'Shortlisted for Interview'), ('Selected', 'Selected'), ('Rejected', 'Rejected')], default='Draft', max_length=30)),
                ('previous_status', models.CharField(max_length=30)),
                ('submitted_at', models.DateTimeField(null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
