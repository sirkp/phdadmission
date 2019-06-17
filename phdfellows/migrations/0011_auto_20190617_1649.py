# Generated by Django 2.2 on 2019-06-17 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phdfellows', '0010_auto_20190617_1631'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='branch_code_for_qualifying_exam',
            field=models.CharField(choices=[('', 'Select'), ('CSE', 'CSE'), ('EE', 'EE'), ('ME', 'ME'), ('ECE', 'ECE'), ('CE', 'CE')], default='Select', max_length=10),
        ),
        migrations.AlterField(
            model_name='application',
            name='category',
            field=models.CharField(choices=[('SC', 'SC'), ('', 'Select'), ('OBC', 'OBC'), ('ST', 'ST'), ('EWS', 'EWS'), ('General', 'General')], default='Select', max_length=10),
        ),
        migrations.AlterField(
            model_name='application',
            name='enrollment_type',
            field=models.CharField(choices=[('', 'Select'), ('Full time', 'Full time'), ('Part time', 'Part time')], default='Select', max_length=50),
        ),
        migrations.AlterField(
            model_name='application',
            name='gender',
            field=models.CharField(choices=[('', 'Select'), ('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], default='Select', max_length=20),
        ),
        migrations.AlterField(
            model_name='application',
            name='pg_discipline',
            field=models.CharField(choices=[('', 'Select'), ('CSE', 'CSE'), ('EE', 'EE'), ('ME', 'ME'), ('ECE', 'ECE'), ('CE', 'CE')], default='Select', max_length=50, verbose_name='PG Discipline'),
        ),
        migrations.AlterField(
            model_name='application',
            name='qualifying_examination',
            field=models.CharField(choices=[('', 'Select'), ('GATE', 'GATE'), ('NET', 'NET')], default='Select', max_length=20),
        ),
        migrations.AlterField(
            model_name='application',
            name='research_area',
            field=models.CharField(choices=[('', 'Select'), ('Machine Learning', 'Machine Learning'), ('Cloud Computing', 'Cloud Computing'), ('Airtifial Intelligence', 'Airtifial Intelligence'), ('Software Development', 'Software Development'), ('Cryptography', 'Cryptography')], default='Select', max_length=50),
        ),
        migrations.AlterField(
            model_name='application',
            name='scale_of_score_pg',
            field=models.CharField(choices=[('', 'Select'), ('0-5 CGPA', '0-5 CGPA'), ('0-10 CGPA', '0-10 CGPA'), ('0-100%', '0-100%')], default='Select', max_length=20, verbose_name='Scale of Score'),
        ),
        migrations.AlterField(
            model_name='application',
            name='scale_of_score_ug',
            field=models.CharField(choices=[('', 'Select'), ('0-5 CGPA', '0-5 CGPA'), ('0-10 CGPA', '0-10 CGPA'), ('0-100%', '0-100%')], default='Select', max_length=20, verbose_name='Scale of Score'),
        ),
        migrations.AlterField(
            model_name='application',
            name='type_of_work',
            field=models.CharField(choices=[('', 'Select'), ('Teaching', 'Teaching'), ('IT Industry', 'IT Industry'), ('Research Organisation', 'Research Organisation'), ('Other', 'Other')], default='Select', max_length=50),
        ),
        migrations.AlterField(
            model_name='application',
            name='ug_discipline',
            field=models.CharField(choices=[('', 'Select'), ('CSE', 'CSE'), ('EE', 'EE'), ('ME', 'ME'), ('ECE', 'ECE'), ('CE', 'CE')], default='Select', max_length=20, verbose_name='UG Discipline'),
        ),
    ]
