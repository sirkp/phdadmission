# Generated by Django 2.2 on 2019-07-04 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phdfellows', '0006_auto_20190704_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='is_branch_code_for_qualifying_exam_other',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='application',
            name='is_pg_discipline_other',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='application',
            name='is_research_area_other',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='application',
            name='is_type_of_work_other',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='application',
            name='is_ug_discipline_other',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='application',
            name='research_area',
            field=models.CharField(default='Select', max_length=50),
        ),
        migrations.AlterField(
            model_name='application',
            name='type_of_work',
            field=models.CharField(default='Select', max_length=100),
        ),
    ]